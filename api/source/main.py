from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.schemas.reservations import Reservation
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

@app.post("/reservations")
async def create_reservation(reservation: Reservation):
  return {"message": "Reservation created successfully"}


@app.get("/holidays", response_model=Holidays)
async def get_holidays(holidays: Holidays):
  return {"holidays": ["2021-01-01", "2021-07-04", "2021-12-25"]}