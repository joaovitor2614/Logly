from faker import Faker




def test_register_user(app):
    fake = Faker()
    mock_new_user_data = {"name": fake.name(), "email": fake.email(), "password": fake.password()}
    response = client.post(
        "/auth/register",
        json={mock_new_user_data},
    )
    print('response', response.status_code)
    print('response.json() ', response.json())
    