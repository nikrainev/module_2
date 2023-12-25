from datetime import datetime

from dataclasses import dataclass

@dataclass
class CreateUserArgs:
    username: str
    firstName: str
    lastName: str
    city: str
    country: str

def User(user_data:CreateUserArgs):
    return {
        'createdAt': datetime.now(),
        'username': user_data.username,
        'firstName': user_data.firstName,
        'lastName': user_data.lastName,
        'city': user_data.city,
        'country': user_data.country
    }