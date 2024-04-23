import re
from pydantic import BaseModel

class PhoneNumber(BaseModel):
    def __init__(self, phone_number) -> None:
        pattern = r"^0\d{10,11}$"

        if not re.match(pattern, phone_number):
            raise ValueError("Invalid phone number")

        self.phone_number = phone_number