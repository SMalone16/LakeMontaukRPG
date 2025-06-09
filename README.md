# Lake Montauk RPG

This repository contains tools to support the Lake Montauk text RPG. It provides a small API for persisting world state (players, locations, items and quests) as well as a dice and skill-check engine with deterministic logs.

## Requirements
- Python 3.12+
- `pip` for installing dependencies

## Setup
```bash
pip install -r requirements.txt
```

## Running the API
```bash
uvicorn app.main:app --reload
```
The API will start on `http://localhost:8000/`.

## Endpoints
- `POST /players` – create a player
- `GET /players` – list players
- `POST /locations` – create a location
- `POST /items` – create an item
- `POST /quests` – create a quest
- `GET /dice/roll/{sides}` – roll a die (e.g. d20)
- `GET /dice/skill-check?stat=5&diff=12` – quick skill check

All dice rolls are recorded in the `roll_logs` table for transparency.
