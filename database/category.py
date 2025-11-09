from sqlalchemy import String, Column, Integer, DateTime
from datetime import timezone,timedelta
from sqlalchemy.sql.expression import true
from sqlalchemy.sql import func
from database.db import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer,primary_key=True)
    title = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(DateTime(timezone=True),server_default=func.now(),onupdate=func.now())