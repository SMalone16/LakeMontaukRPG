from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    location = Column(String, default="")

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text, default="")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, default="")
    location_id = Column(Integer, ForeignKey("locations.id"))
    owner_id = Column(Integer, ForeignKey("players.id"))

class Quest(Base):
    __tablename__ = "quests"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, default="")
    status = Column(String, default="open")
    player_id = Column(Integer, ForeignKey("players.id"))

class RollLog(Base):
    __tablename__ = "roll_logs"
    id = Column(Integer, primary_key=True, index=True)
    roller = Column(String, index=True)
    roll_type = Column(String, index=True)
    result = Column(Integer)
    detail = Column(String)
