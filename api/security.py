# api/security.py
from fastapi import Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader

API_KEY = "2328"
api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
