from pydantic import BaseModel
from typing import Optional

class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    geass: Optional[str] = None
    affiliation: Optional[str] = None
    image: Optional[str] = None