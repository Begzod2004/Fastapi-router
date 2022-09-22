from sqlalchemy.orm import Session
from .models import Cotigory
from .schemas import CotigorySchema

def get_cotigory(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cotigory).offset(skip).limit(limit).all()


def get_cotigory_by_id(db: Session, cotigory_id: int):
    return db.query(Cotigory).filter(Cotigory.id == cotigory_id).first()


def create_cotigory(db: Session, name: str,status: bool, description: str ):
    _cotigory = Cotigory(name=name, status=status, description=description)
    db.add(_cotigory)
    db.commit()
    db.refresh(_cotigory)
    return _cotigory


def remove_cotigory(db: Session, cotigory_id: int):
    _cotigory = get_cotigory_by_id(db=db, cotigory_id=cotigory_id)
    db.delete(_cotigory)
    db.commit()


def update_cotigory(db: Session, cotigory_id: int, name: str, status: int, description: str):
    _cotigory = get_cotigory_by_id(db=db, cotigory_id=cotigory_id)

    _cotigory.name = name
    _cotigory.status = status
    _cotigory.description = description

    db.commit()
    db.refresh(_cotigory)
    return _cotigory