from pydantic import BaseModel
from typing import List, Optional


class CinemaIn(BaseModel):
    name: str
    description: str
    visitors: str
    address: str
    movie_id: List[int]


class CinemaOut(CinemaIn):
    id: int


class ArtistUpdate(CinemaIn):
    name: Optional[str] = None
    age: Optional[str] = None
    auditions: Optional[str] = None
    genre: Optional[str] = None
    movie_id: Optional[List[int]] = None