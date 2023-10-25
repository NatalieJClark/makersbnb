from dataclasses import dataclass


@dataclass
class User:
    """Base User class"""

    id: int
    email: str
    password: str

    def __repr__(self):
        return f"{self.id}, {self.email}, {self.password}"
