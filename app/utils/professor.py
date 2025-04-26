from randomuser import RandomUser
from ..models.professor.professor import Comment, Professor
from faker import Faker
import random

def create_new_fake_professors(amount: int):
    """
    Creates a list of fake professors with given amount of items.

    :param int amount: amount of fake professors to create
    :return: list of dictionaries, each dictionary is a fake professor
    """
    fake = Faker()
    user_list = RandomUser.generate_users(amount)
    return [
            
            Professor(
                name=fake.name(),
                image=user.get_picture(),
                disciplines=[fake.job(), fake.job()],
                gender=user.get_gender(),
                email=user.get_email(),
            )
            
           
        
        for user in user_list
    ]


