from sqlalchemy import Column, Integer, String, Date

from source.db import Base

class Reservations(Base):
  __tablename__ = 'reservations'

  id = Column(Integer, primary_key=True, index=True)
  date = Column(Date)
  name = Column(String(255))
  email_address = Column(String(255))
  phone_number = Column(String(15))
