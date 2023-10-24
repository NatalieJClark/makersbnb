from dataclasses import dataclass

@dataclass
class Space():
    """
    Stores a space's details
    Related to the User class
    """
    id: int
    name: str
    description: str
    size: int
    location: str
    price: float
    user_id: int

    def __repr__(self):
        return "{name} - {location}, £{price:.2f}".format(
            name = self.name, location = self.location, price = self.price)
    