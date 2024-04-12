from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.schemas.reservations import Reservation, ResponseReservation
from source.schemas.holidays import Holidays

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
async def create_reservation(reservation: Reservation):
  return {
    "id": 1,
    "date": "2024-01-01",
    "name": "テスト　ヨヤク",
    "email_address": "example@example.com",
    "phone_number": "123-456-7890"
  }

@app.get("/holidays", response_model=Holidays)
async def get_holidays():
  return {"holidays": ["2021-01-01", "2021-07-04", "2021-12-25"]}

@app.post("/holidays", response_model=Holidays)
async def store_holidays(holidays: Holidays):
  return {"holidays": ["2021-01-01", "2021-07-04", "2021-12-25"]}