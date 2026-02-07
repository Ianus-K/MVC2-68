from dataclasses import dataclass

@dataclass
class Shelter:
    id: int
    code: str
    name: str
    capacity: int
    current_occupancy: int
    risk_level: str