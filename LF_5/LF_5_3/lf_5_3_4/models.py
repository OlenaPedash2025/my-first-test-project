from typing import TypedDict

class Exhibit(TypedDict):
    exhibit_title: str
    creation_year: int
    is_on_display: bool
    weight_kg: float