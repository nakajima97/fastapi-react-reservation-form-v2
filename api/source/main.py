from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from source.db import get_db

from source.schemas.reservations import Reservation, ResponseReservation, GetReservationResponse
from source.schemas.holidays import Holidays

from source.cruds.reservations import store_reservations
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

@app.get("/reservations", response_model=GetReservationResponse)
async def get_reservations(db: Session = Depends(get_db)):
  return [{
        "id": 1,
        "date": "2024-04-13",
        "name": "John Doe",
        "email_address": "example@example.com",
        "phone_number": "123-4567-8901",
    }]

@app.post("/reservations", response_model=ResponseReservation)
async def create_reservation(reservation: Reservation, db: Session = Depends(get_db)):
  reservation = await store_reservations(db, reservation)
  return reservation

@app.get("/holidays", response_model=Holidays)
async def get_holidays(db: Session = Depends(get_db)):
  return await fetch_holidays(db)

@app.post("/holidays", response_model=Holidays)
async def store_holidays(holidays: Holidays, db: Session = Depends(get_db)):
  calendar = await store_calendars(db, holidays)
  return calendar