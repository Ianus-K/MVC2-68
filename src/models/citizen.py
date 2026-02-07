from dataclasses import dataclass
from datetime import datetime

@dataclass
class Citizen:
    id: int
    citizen_id: str
    first_name: str
    last_name: str
    age: int
    gender: str
    health_condition: str
    category: str
    registered_at: datetime

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"