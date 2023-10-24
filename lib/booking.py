from dataclasses import dataclass

@dataclass
class Booking():
    # Stores details of a Booking
    id: int
    confirmed: bool
    space_id: int
    date_id: int
    guest_id: int
    owner_id: int