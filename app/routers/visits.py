from fastapi import APIRouter, HTTPException

from app.postgres_setup import Session, engine, MySiteVisits
from app.models import VisitData


router = APIRouter(
    prefix="/visits",
    tags=["site_visits"],
)


def save_visit_to_database(visit_data: VisitData):
    with Session(engine) as session:
        session.add(MySiteVisits(**dict(visit_data)))
        session.commit()


@router.post("")
def register_site_interaction(visit_data: VisitData):
    try:
        save_visit_to_database(visit_data)
    except:
        raise HTTPException(status_code=500, detail="Couldn't register user interaction.")