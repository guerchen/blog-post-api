from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

class Post(BaseModel):
    title: str
    date: date
    content: str

class VisitData(BaseModel):
    page: str
    date: datetime
    ip: str
    hostname: Optional[str]
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]
    loc: Optional[str]
    org: Optional[str]
    postal: Optional[str]
    timezone: Optional[str]