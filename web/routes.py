from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .database import SessionLocal
from sqlalchemy.orm import Session
from .schemas import  Response, RequestCotigoryUpdate, RequestCotigoryCreate, RequestCotigoryDelete
from . import crud
from . import models

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
async def get(db:Session=Depends(get_db)):
  _cotigory = crud.get_cotigory(db, 0, 100)
  return Response(code=200, status='Ok', message='Success Fetch all data', result=_cotigory).dict(exclude_none=True)

@router.get('/{id}')
async def get_by_id(id: int, db:Session=Depends(get_db)):
  _cotigory = crud.get_cotigory_by_id(db, cotigory_id=id)
  return Response(code=200, status='Ok', message='Success get data', result=_cotigory).dict(exclude_none=True)

@router.post("/create")
async def create_cotigory_service(request: RequestCotigoryCreate, db: Session = Depends(get_db)):
    crud.create_cotigory(db, cotigory=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Book created successfully").dict(exclude_none=True)


@router.patch("/update")
async def update_cotigory(request: RequestCotigoryUpdate, db: Session = Depends(get_db)):
    _cotigory = crud.update_cotigory(db, cotigory_id=request.parameter.id,
                             name=request.parameter.name, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Success update data", result=_cotigory)


@router.delete("/delete/{id}")
async def delete_cotigory(id: int, db: Session = Depends(get_db)):
    crud.remove_cotigory(db, cotigory_id=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

