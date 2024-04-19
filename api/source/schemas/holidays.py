from pydantic import BaseModel, Field
from typing import List
import datetime

class Holidays(BaseModel):
    holidays: List[datetime.date] = Field(..., title="List of dates that are holidays")

    model_config = {
        "json_schema_extra": {
            "examples": [{
                "holidays": ["2024-05-01", "2024-05-02", "2024-05-05"]
            }]
        }
    }