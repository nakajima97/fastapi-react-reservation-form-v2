from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.db import get_db
from source.schemas.holidays import Holidays
from source.cruds.calendars import store_holidays, fetch_holidays

router = APIRouter()

@router.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return await fetch_holidays(db)

@router.post("/holidays", response_model=Holidays)
async def post_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  calendar = await store_holidays(db, holidays)
  return calendar