from database.db import Base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import Integer, String, ForeignKey, DateTime, func, Boolean
import uuid

class TimeMixin(Base):
    @declared_attr
    def created_at(cls):
        return mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)

    @declared_attr
    def updated_at(cls):
        return mapped_column(DateTime(timezone=True),server_onupdate=func.now(),server_default=func.now(),nullable=False)

class User(Base,TimeMixin):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True,default=uuid.uuid4)
    username:Mapped[String] = mapped_column(String,unique=True,nullable=False)
    email:Mapped[String] = mapped_column(String,unique=True,nullable=False)
    password:Mapped[String] = mapped_column(String,nullable=False)
    active:Mapped[bool] = mapped_column(Boolean,nullable=False)
