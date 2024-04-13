from sqlalchemy.ext.asyncio import AsyncSession

import source.models.calendars as calendars_model
import source.schemas.holidays as holidays_schema

async def store_calendars(db: AsyncSession, holidays: holidays_schema.Holidays) -> calendars_model.Calendars:
    for holiday in holidays.holidays:
        calendar = calendars_model.Calendars(date=holiday, is_holiday=True)
        db.add(calendar)
    await db.commit()
    return holidays