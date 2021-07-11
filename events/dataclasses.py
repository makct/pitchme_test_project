from dataclasses import dataclass
from datetime import date


@dataclass
class SearchParams:
    city: str
    topic: str
    start_interval: date
    end_interval: date
