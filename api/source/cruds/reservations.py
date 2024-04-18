from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

import source.models.reservations as reservations_model
import source.schemas.reservations as reservations_schema

async def store_reservations(db: AsyncSession, reservation: reservations_schema.Reservation) -> reservations_model.Reservations:
    reservation = reservations_model.Reservations(**reservation.model_dump())
    db.add(reservation)
    await db.commit()
    await db.refresh(reservation)
    return reservation

async def fetch_reservations(db):
    result = await db.execute(select(reservations_model.Reservations))
    result_all = result.all()
    reservations = [reservation[0] for reservation in result_all]

    return {'reservations': reservations}