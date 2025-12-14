from faker import Faker
import json
from faker import Faker
from ..utils.security import verify_password
from app.tests.utils.wrapper.auth import AuthEndPointWrapper
from app.controllers.user import UserController
from app.tests.utils.auth import get_user_id_from_register_response
import pytest



class TestRegister:
    @pytest.fixture(autouse=True)
    def setup(self, client):
        self.client = client
        self.auth_endpoint_mocker = AuthEndPointWrapper(self.client)
        self.user_controller = UserController(client)

    def test_register_user(self):
        fake = Faker()
        mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
        response = self.auth_endpoint_mocker.register(mock_new_user_data)


        assert response.status_code == 201, f"Response status code expected to be 201, but got {response.status_code}"
        response_content = response.json()

        assert response_content["token"] is not None, "Token not present auth endpoint response."

        
        user_id = get_user_id_from_register_response(response)

        new_user = self.user_controller.get_user_by_id(user_id)
        
        assert verify_password(mock_new_user_data["password"], new_user["password"]), "Password not hashed correctly"
        assert new_user["email"] == mock_new_user_data["email"], "Email not stored correctly"
        assert new_user["name"] == mock_new_user_data["name"], "Name not stored correctly"


   

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, client, register_user):
        self.client = client
        self.auth_endpoint_mocker = AuthEndPointWrapper(self.client)
        self.mock_new_user_data, _ = register_user
    def test_login_user(self):


        response = self.auth_endpoint_mocker.login(self.mock_new_user_data["email"], self.mock_new_user_data["password"])
        self.assert_response_info(response, 201)
        assert "token" in response.json()

    def test_login_wrong_password(self):
        response = self.auth_endpoint_mocker.login(self.mock_new_user_data["email"], "coxinha123")
        self.assert_response_info(response, 401, "Password is not valid!")

    def test_login_non_existent_user(self):
        response = self.auth_endpoint_mocker.login("2B2Gd@example.com", "coxinha123")
        self.assert_response_info(response, 404, "User not found!")


    def assert_response_info(self, response, expected_code: int, expected_text: str = ''):
        assert response.status_code == expected_code
        if expected_text:
            response_text = json.loads(response.text)["detail"]
            assert response_text == expected_text

        












