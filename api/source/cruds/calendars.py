from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import source.models.calendars as calendars_model
import source.schemas.holidays as holidays_schema

async def store_holidays(db: AsyncSession, holidays: holidays_schema.Holidays) -> calendars_model.Calendars:
    for holiday in holidays.holidays:
        result = await db.execute(select(calendars_model.Calendars.date).filter(calendars_model.Calendars.date == holiday))
        if result.scalar() is not None:
            continue

        calendar = calendars_model.Calendars(date=holiday, is_holiday=True)
        db.add(calendar)
    await db.commit()
    return holidays

async def fetch_holidays(db: AsyncSession) -> holidays_schema.Holidays:
    result = await db.execute(select(calendars_model.Calendars.date).filter(calendars_model.Calendars.is_holiday == True))
    holidays = result.all()

    return {'holidays': [holiday[0] for holiday in holidays]}