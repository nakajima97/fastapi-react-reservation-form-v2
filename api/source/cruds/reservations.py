from sqlalchemy.ext.asyncio import AsyncSession

import source.models.reservations as reservations_model
import source.schemas.reservations as reservations_schema

async def store_reservations(db: AsyncSession, reservation: reservations_schema.Reservation) -> reservations_model.Reservations:
    reservation = reservations_model.Reservations(**reservation.dict())
    db.add(reservation)
    await db.commit()
    await db.refresh(reservation)
    return reservation