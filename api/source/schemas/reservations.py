from pydantic import BaseModel, Field
import datetime

class Reservation(BaseModel):
    date: datetime.date = Field(..., title="Date of the reservation", examples="2024-01-01")
    name: str = Field(..., title="Name of the person making the reservation", examples="テスト　ヨヤク")
    email_address: str = Field(..., title="Email of the person making the reservation", examples="example@example.com")
    phone_number: str = Field(..., title="Phone number of the person making the reservation", examples="123-456-7890")

class ResponseReservation(Reservation):
    id: int = Field(..., title="ID of the reservation", example=1)