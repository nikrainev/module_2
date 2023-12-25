from dataclasses import dataclass

@dataclass
class CreateUserRequest:
    username: str
    firstName: str
    lastName: str
    ip: str