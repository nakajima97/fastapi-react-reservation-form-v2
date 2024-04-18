from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from source.db import get_db

from source.schemas.reservations import Reservation, ResponseReservation, GetReservationResponse
from source.cruds.reservations import store_reservations, fetch_reservations


router = APIRouter()

@router.get("/reservations", response_model=GetReservationResponse)
async def get_reservations(db: Session = Depends(get_db)):
  return await fetch_reservations(db)

@router.post("/reservations", response_model=ResponseReservation)
async def create_reservation(reservation: Reservation, db: Session = Depends(get_db)):
  reservation = await store_reservations(db, reservation)
  return reservation