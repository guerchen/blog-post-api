from datetime import date, datetime

from pydantic import BaseModel

class Post(BaseModel):
    title: str
    date: date
    content: str

class VisitData(BaseModel):
    page: str
    date: datetime
    ip: str
    hostname: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str
    timezone: str