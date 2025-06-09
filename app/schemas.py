from pydantic import BaseModel

class PlayerBase(BaseModel):
    name: str
    location: str | None = None

class PlayerCreate(PlayerBase):
    pass

class Player(PlayerBase):
    id: int
    class Config:
        orm_mode = True

class LocationBase(BaseModel):
    name: str
    description: str | None = None

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int
    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    name: str
    description: str | None = None
    location_id: int | None = None
    owner_id: int | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    class Config:
        orm_mode = True

class QuestBase(BaseModel):
    name: str
    description: str | None = None
    status: str | None = None
    player_id: int | None = None

class QuestCreate(QuestBase):
    pass

class Quest(QuestBase):
    id: int
    class Config:
        orm_mode = True

class RollResult(BaseModel):
    roller: str
    roll_type: str
    result: int
    detail: str
    class Config:
        orm_mode = True
