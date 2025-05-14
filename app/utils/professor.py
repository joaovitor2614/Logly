from randomuser import RandomUser
from ..models.professor.professor import Comment, Professor
from faker import Faker
import random

def create_new_fake_professor(faker_instance: Faker | None = None) -> Professor:
    if faker_instance is None:
        faker_instance = Faker()
    return Professor(
        name=faker_instance.name(),
        image=faker_instance.image_url(),
        disciplines=['Calculo IV'],
        gender='other',
        email=faker_instance.email(),
        phone=faker_instance.phone_number()
    )
