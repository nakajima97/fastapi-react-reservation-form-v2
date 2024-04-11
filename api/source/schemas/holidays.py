from pydantic import BaseModel, Field
from typing import List
import datetime

class Holidays(BaseModel):
  holidays: List[datetime.date] = Field(..., title="List of dates that are holidays", example=["2021-01-01", "2021-07-04", "2021-12-25"])