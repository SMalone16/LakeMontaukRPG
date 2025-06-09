from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/locations", tags=["locations"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    db_location = models.Location(name=location.name, description=location.description or "")
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("/", response_model=list[schemas.Location])
def read_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@router.get("/{location_id}", response_model=schemas.Location)
def read_location(location_id: int, db: Session = Depends(get_db)):
    loc = db.query(models.Location).filter(models.Location.id == location_id).first()
    if loc is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc

@router.put("/{location_id}", response_model=schemas.Location)
def update_location(location_id: int, location: schemas.LocationCreate, db: Session = Depends(get_db)):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db_location.name = location.name
    db_location.description = location.description or db_location.description
    db.commit()
    db.refresh(db_location)
    return db_location

@router.delete("/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return {"ok": True}
