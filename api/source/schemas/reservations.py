from pydantic import BaseModel, Field
import datetime

class Reservation(BaseModel):
    date: datetime.date = Field(..., title="Date of the reservation")
    name: str = Field(..., title="Name of the person making the reservation")
    email_address: str = Field(..., title="Email of the person making the reservation")
    phone_number: str = Field(..., title="Phone number of the person making the reservation")