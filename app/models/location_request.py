from pydantic import BaseModel, field_validator
import re


class LocationRequest(BaseModel):
    reqId: str
    ip: str

    # Check if `reqId` field is empty or whitespace
    @field_validator("reqId")
    def validate_reqId(cls, value):
        if not value.strip():
            raise ValueError("reqId cannot be an empty string")
        return value

    # Check if the `ip` field is in a valid IP address format
    @field_validator("ip")
    def validate_ip(cls, value):
        ip_regex = (
            r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
        )

        if not re.match(ip_regex, value):
            raise ValueError("Invalid IP address format")
        return value
