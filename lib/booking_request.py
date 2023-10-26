from dataclasses import dataclass

@dataclass
class BookingRequest:
    """Base booking_request class"""

    id: int
    confirmed: bool
    space_id: int
    date_id: int
    guest_id: int
    owner_id: int

    def __repr__(self):
        return f"Booking Request({self.id}, {self.confirmed}, {self.space_id}, {self.date_id}, {self.guest_id}, {self.owner_id})"