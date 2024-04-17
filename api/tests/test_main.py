import pytest
import pytest_asyncio
import starlette.status

from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from source.db import get_db, Base
from source.main import app

ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_reservation(async_client):
    base_json = {
        "date": "2024-01-01",
        "name": "テスト　ヨヤク",
        "email_address": "example@example.com",
        "phone_number": "123-456-7890"
    }
    response = await async_client.post("/reservations", json=base_json)
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["date"] == base_json["date"]
    assert response_object["name"] == base_json["name"]
    assert response_object["email_address"] == base_json["email_address"]
    assert response_object["phone_number"] == base_json["phone_number"]
    assert response_object["id"] == 1

@pytest.mark.asyncio
async def test_create_holidays(async_client):
    base_json = {
        "holidays": ["2024-01-01", "2024-01-02"]
    }
    response = await async_client.post("/holidays", json=base_json)
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["holidays"] == base_json["holidays"]

@pytest.mark.asyncio
async def test_get_holidays_no_data(async_client):
    response = await async_client.get("/holidays")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["holidays"] == []

@pytest.mark.asyncio
async def test_post_holidays_and_get_holidays(async_client):
    base_json = {
        "holidays": ["2024-01-01", "2024-01-02"]
    }
    await async_client.post("/holidays", json=base_json)
    response = await async_client.get("/holidays")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_object = response.json()
    assert response_object["holidays"] == base_json["holidays"]