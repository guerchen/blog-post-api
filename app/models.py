from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

class Post(BaseModel):
    title: str
    date: date
    content: str

class VisitData(BaseModel):
    page: str
    date: datetime
    ip: str
    hostname: Optional[str] = Field(default=None)
    city: Optional[str] = Field(default=None)
    region: Optional[str] = Field(default=None)
    country: Optional[str] = Field(default=None)
    loc: Optional[str] = Field(default=None)
    org: Optional[str] = Field(default=None)
    postal: Optional[str] = Field(default=None)
    timezone: Optional[str] = Field(default=None)