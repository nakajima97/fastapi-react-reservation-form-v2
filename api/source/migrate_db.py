from sqlalchemy import create_engine

DB_URL = "mysql+pymysql://root@mysql:3306/reservation_form"
engine = create_engine(DB_URL, echo=True)

def reset_database():
  pass

if __name__ == "__main__":
  reset_database()