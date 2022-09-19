from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from sqlalchemy import  Column, Integer

T = TypeVar('T')


class CotigorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class CotigorySchemaCreate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class CotigorySchemaDelete(BaseModel):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestCotigoryCreate(BaseModel):
    parameter: CotigorySchemaCreate = Field(...)

class RequestCotigoryUpdate(BaseModel):
    parameter: CotigorySchema = Field(...)

class RequestCotigoryDelete(BaseModel):
    parameter: CotigorySchemaDelete = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
