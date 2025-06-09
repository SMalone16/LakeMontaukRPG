from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/quests", tags=["quests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Quest)
def create_quest(quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    db_quest = models.Quest(**quest.dict())
    db.add(db_quest)
    db.commit()
    db.refresh(db_quest)
    return db_quest

@router.get("/", response_model=list[schemas.Quest])
def read_quests(db: Session = Depends(get_db)):
    return db.query(models.Quest).all()

@router.get("/{quest_id}", response_model=schemas.Quest)
def read_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = db.query(models.Quest).filter(models.Quest.id == quest_id).first()
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    return quest

@router.put("/{quest_id}", response_model=schemas.Quest)
def update_quest(quest_id: int, quest: schemas.QuestCreate, db: Session = Depends(get_db)):
    db_quest = db.query(models.Quest).filter(models.Quest.id == quest_id).first()
    if db_quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    for key, value in quest.dict().items():
        setattr(db_quest, key, value)
    db.commit()
    db.refresh(db_quest)
    return db_quest

@router.delete("/{quest_id}")
def delete_quest(quest_id: int, db: Session = Depends(get_db)):
    quest = db.query(models.Quest).filter(models.Quest.id == quest_id).first()
    if quest is None:
        raise HTTPException(status_code=404, detail="Quest not found")
    db.delete(quest)
    db.commit()
    return {"ok": True}
