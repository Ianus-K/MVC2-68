from dataclasses import dataclass
from datetime import datetime

@dataclass
class Assignment:
    id: int
    citizen_id: str
    shelter_code: str
    assigned_at: datetime