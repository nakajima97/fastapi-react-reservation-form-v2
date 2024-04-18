from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from source.routers import reservations, holidays

app = FastAPI()

origins = [
  'http://localhost:5173',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(reservations.router)
app.include_router(holidays.router)