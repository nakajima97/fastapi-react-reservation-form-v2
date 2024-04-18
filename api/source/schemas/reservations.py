from pydantic import BaseModel, Field
import datetime

class Reservation(BaseModel):
    date: datetime.date = Field(..., title="Date of the reservation")
    name: str = Field(..., title="Name of the person making the reservation")
    email_address: str = Field(..., title="Email of the person making the reservation")
    phone_number: str = Field(..., title="Phone number of the person making the reservation")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "date": "2024-04-13",
                    "name": "John Doe",
                    "email_address": "example@example.com",
                    "phone_number": "123-4567-8901",
                }
            ]
        }
    }

class ResponseReservation(Reservation):
    id: int = Field(..., title="ID of the reservation")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "date": "2024-04-13",
                    "name": "John Doe",
                    "email_address": "example@example.com",
                    "phone_number": "123-4567-8901",
                }
            ]
        }
    }

class GetReservationResponse(BaseModel):
    reservations: list[ResponseReservation]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "reservations": [
                        {
                            "id": 1,
                            "date": "2024-04-13",
                            "name": "John Doe",
                            "email_address": "example@example.com"
                        },
                        {
                            "id": 2,
                            "date": "2024-04-30",
                            "name": "Deborah Doe",
                            "email_address": "example@example.com"
                        },
                    ]
                }
            ]
        }
    }
