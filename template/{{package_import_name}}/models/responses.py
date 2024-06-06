"""FastAPI response models."""
from typing import Any

from fastapi import status
from pydantic import BaseModel, Field


class HTTPError(BaseModel):
    """HTTP error response class."""
    detail: str = Field(examples=["HTTPException raised."])


def generate_http_error_response(status_code: int, detail: str) -> dict[int | str, dict[str, Any]]:
    """Generate HTTP error response."""
    return {status_code: {"model": HTTPError, "description": detail,
                          "content": {"application/json": {"example": {"detail": detail}}}}}


http_204_deleted = generate_http_error_response(status.HTTP_204_NO_CONTENT, "Object deleted.")
http_400_bad_request = generate_http_error_response(status.HTTP_400_BAD_REQUEST, "Bad request.")
http_401_unauthorized = generate_http_error_response(status.HTTP_401_UNAUTHORIZED, "Unauthorized.")
http_403_forbidden = generate_http_error_response(status.HTTP_403_FORBIDDEN, "Forbidden.")
http_404_not_found = generate_http_error_response(status.HTTP_404_NOT_FOUND, "Object not found.")
http_409_already_exists = generate_http_error_response(status.HTTP_409_CONFLICT, "Object already exists.")
http_500_internal_server_error = generate_http_error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error.")
