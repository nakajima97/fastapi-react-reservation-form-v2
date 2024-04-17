from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from source.db import Base

class Reservations(Base):
  __tablename__ = 'reservations'

  id = Column(Integer, primary_key=True, index=True)
  date = Column(Date)
  name = Column(String(255))
  email_address = Column(String(255))
  phone_number = Column(String(15))
  created_at = Column(DateTime, nullable=False, default=func.now())
  updated_at = Column(DateTime, nullable=False, default=func.now())