import os
from typing import Optional
from datetime import datetime

from sqlmodel import Field, Session, SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()
postgres_conn_string = os.getenv("POSTGRES_CONN_STRING")

engine = create_engine(postgres_conn_string, echo=True)

class MySiteVisits(SQLModel, table=True):
    __tablename__ = "my_site_interactions"

    id: Optional[int] = Field(primary_key=True)
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
