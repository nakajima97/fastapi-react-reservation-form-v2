from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from source.routers import reservations

from source.db import get_db

from source.schemas.holidays import Holidays

from source.cruds.calendars import store_calendars, fetch_holidays

app = FastAPI()

origins = [
  'http://localhost:5173',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(reservations.router)

@app.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return await fetch_holidays(db)

@app.post("/holidays", response_model=Holidays)
async def store_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  calendar = await store_calendars(db, holidays)
  return calendar