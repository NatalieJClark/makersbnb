from dataclasses import dataclass

@dataclass
class Date():
    """
    Stores a date's details
    Related to the Space class
    """
    id: int
    date: str
    available: bool
    space_id: int
    
    def __repr__(self):
        return f"Date({self.id}, {self.date}, {self.available}, {self.space_id})"