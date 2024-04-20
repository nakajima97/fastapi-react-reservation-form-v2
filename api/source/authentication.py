from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

from source.config import settings

api_key_header = APIKeyHeader(name='X-API-Key')

def get_api_key_from_header(api_key: str = Depends(api_key_header)):
    if api_key == settings.API_KEY:
        return api_key

    raise HTTPException(status_code=403)