from sqlalchemy import String, Column, BigInteger, DateTime
from datetime import timezone,timedelta
from sqlalchemy.sql.expression import true
from sqlalchemy.sql import func
from database.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(BigInteger,primary_key=True)
    name = Column(String)
    username = Column(String)
    phone_number = Column(String)
    login = Column(String)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())