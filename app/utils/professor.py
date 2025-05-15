from randomuser import RandomUser
from ..models.professor.professor import Comment, Professor
from faker import Faker
import random

def create_new_fake_professor(faker_instance: Faker | None = None) -> Professor:
    if faker_instance is None:
        faker_instance = Faker()

    professor_gender = 'male' if random.random() >= 0.5  else 'female'
    return Professor(
        name=faker_instance.name(),
        image='https://thispersondoesnotexist.com/',
        disciplines=['Calculo IV'],
        gender=professor_gender,
        email=faker_instance.email(),
        phone=faker_instance.phone_number()
    )
