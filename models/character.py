from typing import Optional
from pydantic import BaseModel

class Character(BaseModel):
    id: Optional[str] = None
    name: str
    geass: str
    affiliation: str
    image: str