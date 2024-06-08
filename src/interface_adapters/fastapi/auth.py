from decouple import config
from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader


def provide_api_key_auth(key_name: str) -> None:

    def api_key_auth(
        api_key: str = Security(APIKeyHeader(name="Authorization")),
    ) -> None:
        if api_key != config(key_name):
            raise HTTPException(status_code=401, detail="Invalid API key")

    return api_key_auth
