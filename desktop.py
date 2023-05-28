from pydantic import BaseModel


class Desktop(BaseModel):
    id: int
    brand: str
    capacity: int
    screensize: float
    price: float