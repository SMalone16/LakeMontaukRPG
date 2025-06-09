import random
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/dice", tags=["dice"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def log_roll(db: Session, roller: str, roll_type: str, result: int, detail: str):
    log = models.RollLog(roller=roller, roll_type=roll_type, result=result, detail=detail)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

@router.get("/roll/{sides}", response_model=schemas.RollResult)
def roll_die(sides: int, db: Session = Depends(get_db), roller: str = "system"):
    result = random.randint(1, sides)
    detail = f"d{sides}"
    log = log_roll(db, roller, detail, result, detail)
    return schemas.RollResult(roller=roller, roll_type=detail, result=result, detail=detail)

@router.get("/skill-check")
def skill_check(stat: int = 10, diff: int = 10, db: Session = Depends(get_db), roller: str = "system"):
    roll = random.randint(1, 20)
    total = roll + stat
    success = total >= diff
    detail = f"stat={stat} diff={diff}"
    log_roll(db, roller, "skill", roll, detail)
    return {"roll": roll, "total": total, "success": success}
