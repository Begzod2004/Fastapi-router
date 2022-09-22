from datetime import datetime
from sqlalchemy import Column, Integer, String , ForeignKey, DateTime, Boolean
from .database import Base
from .chooses import *
import sqlalchemy.types as types 
from sqlalchemy.types import Text 


class ChoiceType(types.TypeDecorator):

    impl = types.String

    def init(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).init(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.iteritems() if v == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]

# class Entity(Base):
#         tablename = "entity"
#         height = Column(
#             ChoiceType({"short": "short", "medium": "medium", "tall": "tall"}), nullable=False
#         )

# Cotigory
class Cotigory(Base):
    __tablename__ = 'cotigors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
    description = Column(Text)

# SubCotigory
class SubCotigory(Base):
     __tablename__ = 'subcotigors'
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, nullable=False)
     description = Column(Text)
     cotigory_id = Column(Integer , ForeignKey("cotigors.id"))
     status = Column(Boolean, nullable=False)

# Product
class Product(Base):
     __tablename__ = 'products'
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, nullable=False)
     image = Column(String, nullable=False) # field with relation with image,
     status = Column(Boolean, nullable=False)
     description = Column(Text, nullable=False)
     level = Column(Integer, nullable=False)
     created = Column(DateTime, default=datetime.utcnow)
     updated = Column(DateTime, default=datetime.utcnow)
     price = Column(Integer, nullable=False)
     sub_cotigory_id = Column(Integer , ForeignKey("subcotigors.id"))
     author = Column(String, nullable=False)

# Content
class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    name = Column(String, nullable=False)
    created = Column(DateTime,default=datetime.utcnow)
    updated = Column(DateTime,default=datetime.utcnow)
    type = Column(String, nullable=False)
    file_name = Column(String, nullable=True)
    type_status = Column(String, nullable=False)
    file_url = Column(String, nullable=True)
    product_id = Column(Integer , ForeignKey("products.id"))
    
# Querys
class Querys(Base):
    __tablename__ = 'querys'
    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, ForeignKey("contents.id"))
    name = Column(String, nullable=False)
    description = Column(Text,nullable=False)
    type = Column(Boolean, nullable=False)
    is_true = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)

# Answare
class Answare(Base):
    __tablename__ = 'answares'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    is_true = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
    query_id = Column(Integer, ForeignKey("querys.id"))