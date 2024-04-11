from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.schemas.reservations import Reservation

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