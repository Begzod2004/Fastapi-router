from typing import Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from sqlalchemy import  Column, Integer
from .models import *

T = TypeVar('T')

# CotigorySchema
class CotigorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[bool] = None
    description: Optional[str] = None
    class Config:
        orm_mode = True


# Sub_CotigorySchema
class SubCotigorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    cotigory: Optional[int] = None
    status: Optional[bool] = None

    class Config:
        orm_mode = True

# ProductSchema
class ProductSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    image: Optional[str] = None
    status: Optional[bool] = None
    description: Optional[str] = None
    level: Optional[str] = None
    created: Optional[str] = None
    updated: Optional[str] = None
    price: Optional[int] = None
    sub_cotigory: Optional[int] = None
    auther: Optional[str] = None
   
    class Config:
        orm_mode = True


# ContentSchema
class ContentSchema(BaseModel):
    id: Optional[int] = None
    product: Optional[int] = None
    name: Optional[str] = None
    created: Optional[int] = None
    updated: Optional[int] = None
    type: Optional[str] = None
    file: Optional[str] = None
    type_status: Optional[str] = None
    file_url: Optional[str] = None
    praduct: Optional[int] = None
    discount: Optional[str] = None
    class Config:
        orm_mode = True


# QuerysSchema
class QuerysSchema(BaseModel):
    id: Optional[int] = None
    content: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    is_true: Optional[str] = None
    status: Optional[bool] = None
    class Config:
        orm_mode = True

# AnswareSchema
class AnswareSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    is_true: Optional[str] = None
    status: Optional[bool] = None
    query: Optional[int] = None

    class Config:
        orm_mode = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

class RequestCotigory(BaseModel):
    parameter: CotigorySchema = Field(...)

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class RequestCotigoryCreate(BaseModel):
    parameter: Optional[T] = Field(...)

class RequestCotigoryUpdate(BaseModel):
    parameter: Optional[T] = Field(...)                       

class RequestCotigoryDelete(BaseModel):
    parameter: Optional[T] = Field(...)
