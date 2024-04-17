from sqlalchemy import Column, Integer, Date, Boolean, DateTime
from sqlalchemy.sql import func
from zoneinfo import ZoneInfo

import datetime

from source.db import Base

class Calendars(Base):
    __tablename__ = 'calendars'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, unique=True)
    is_holiday = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())