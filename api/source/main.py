from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from source.db import get_db

from source.schemas.reservations import Reservation, ResponseReservation
from source.schemas.holidays import Holidays

from source.cruds.reservations import store_reservations

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

@app.post("/reservations", response_model=ResponseReservation)
async def create_reservation(reservation: Reservation, db: Session = Depends(get_db)):
  reservation = await store_reservations(db, reservation)
  return reservation

@app.get("/holidays", response_model=Holidays)
async def get_holidays():
  return {"holidays": ["2021-01-01", "2021-07-04", "2021-12-25"]}

@app.post("/holidays", response_model=Holidays)
async def store_holidays(holidays: Holidays):
  return {"holidays": ["2021-01-01", "2021-07-04", "2021-12-25"]}