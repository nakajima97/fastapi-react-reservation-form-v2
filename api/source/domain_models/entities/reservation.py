from source.domain_models.value_objects.reservation_id import ReservationId
from source.domain_models.value_objects.name import Name
from source.domain_models.value_objects.reservation_date import ReservationDate
from source.domain_models.value_objects.phone_number import PhoneNumber
from source.domain_models.value_objects.email_address import EmailAddress

class Reservation():
    def __init__(
            self,
            id: ReservationId,
            name: Name,
            reservation_date: ReservationDate,
            phone_number: PhoneNumber,
            email_address: EmailAddress
        ) -> None:
        self.id = id
        self.name = name
        self.reservation_date = reservation_date
        self.phone_number = phone_number
        self.email_address = email_address