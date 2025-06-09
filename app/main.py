from fastapi import FastAPI
from .database import Base, engine
from .routers import players, locations, items, quests, dice

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lake Montauk RPG API")

app.include_router(players.router)
app.include_router(locations.router)
app.include_router(items.router)
app.include_router(quests.router)
app.include_router(dice.router)

@app.get("/")
def read_root():
    return {"message": "Lake Montauk RPG API"}
