import collections
from dataclasses import dataclass
from datetime import datetime
from pydoc import describe
import string
from sqlalchemy import Column, Integer, String , ForeignKey
from .database import Base
from .chooses import *



class Cotigory(Base):
    __tablename__ = 'cotigors'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = False
    description = Column(String)

class SubCotigory(Base):
     __tablename__ = 'subcotigors'
     id = Column(Integer, primary_key=True, index=True)
     description = Column(String)
     cotigory_id = Column(Integer , ForeignKey("cotigors.id"))
     status = False




class Product(Base):
     __tablename__ = 'products'
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String)
     image = Column(str) # field with relation with image,
     status = False
     description = Column(String)
     level = Column(Integer)
     created = Column(datetime)
     updated = Column(datetime)
     price = Column(Integer)
     sub_cotigory_id = Column(Integer , ForeignKey("subcotigors.id"))
     author = Column(str)
     




class Pay_type(Base):
     __tablename__ = 'pay_types'
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String)
     number = Column(Integer)
   



class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    created = Column(datetime)
    quanty = Column(Integer)
    total_price = Column(Integer)
    status = Column(Integer,choices=STATIC)
    pay_type_id = Column(Integer , ForeignKey("pay_types.id"))
    product_id = Column(Integer , ForeignKey("subcotigors.id"))




class Order_details(Base):
    __tablename__ = 'order_details'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer , ForeignKey("orders.id"))
    product_id = Column(Integer , ForeignKey("products.id"))




class Discount(Base):
    __tablename__ = 'discounts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    type = Column(String)
    query = Column(String)

class Product_discount(Base):
    __tablename__ = 'product_discounts'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer , ForeignKey("products.id"))
    discount_id = Column(Integer , ForeignKey("discounts.id") )


class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    name = Column(String)
    createed = Column(datetime)
    updated = Column(datetime)
    type = Column(String)
    file = Column()
    type_status = Column()
    file_url = Column()
    product_id = Column(Integer , ForeignKey("products.id"))
    discount_id = Column(Integer , ForeignKey("discounts.id") )




class Querys(Base):
    __tablename__ = 'querys'
    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("contents.id"))
    name = Column(String)
    description = Column(String)
    type = Column(Integer,choices=TYPE)
    is_true = Column()
    status = False


class Answare(Base):
    __tablename__ = 'answares'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_true = Column()
    status = False
    query_id = Column(Integer, ForeignKey("querys.id"))
