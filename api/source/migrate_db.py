from sqlalchemy import create_engine

from source.models.reservations import Reservations

DB_URL = "mysql+pymysql://root@mysql:3306/reservation_form"
engine = create_engine(DB_URL, echo=True)

def reset_database():
  Reservations.metadata.drop_all(engine)
  Reservations.metadata.create_all(engine)

if __name__ == "__main__":
  reset_database()