from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.database.database import get_db
from app.models.incident import Incident as IncidentDB

def create_incident(
    db: Session, item
):
    db_id = db.query(IncidentDB).count() + 1
    
    incident = IncidentDB(
        incident_id = f"INC{db_id:06d}",
        short_description=item.short_description,
        description=item.description,
        criticality=item.criticality,
        status=item.status,
        reporter=item.reporter,
        assigned_to=item.assigned_to,
        service_name=item.service_name,
        environment=item.environment
     )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return incident


def get_incidents(
    db:Session,
    limit: int,
    offset: int,
    status: str | None = None,
    criticality: str | None = None,
    assigned_to: str | None = None,
    
):

    query = db.query(IncidentDB)

    if status:
        query = query.filter(
            IncidentDB.status == status
        )

    if criticality:
        query = query.filter(
            IncidentDB.criticality == criticality
        )

    if assigned_to:
        query = query.filter(
            IncidentDB.assigned_to == assigned_to
        )

    return (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_incident_by_id(
    incident_id: str,
    db: Session
):

    incident = (
        db.query(IncidentDB)
        .filter(
            IncidentDB.incident_id == incident_id
        )
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail=f"Incident {incident_id} not found"
        )

    return incident


def get_dashboard(
    db: Session
):
    return{
    "Total incidents": db.query(
        IncidentDB
    ).count(),

    "Open incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.status == "open"
    ).count(),

    "Resolved incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.status == "resolved"
    ).count(),

    "In progress incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.status == "in progress"
    ).count(),

    "On hold incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.status == "on hold"
    ).count(),

    "Critical incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.criticality == "critical"
    ).count(),

    "High incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.criticality == "high"
    ).count(),

    "Medium incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.criticality == "medium"
    ).count(),

    "Low incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.criticality == "low"
    ).count(),

    "Production incidents":db.query(
        IncidentDB
    ).filter(
        IncidentDB.environment == "production"
    ).count(),

    "Integration incidents":db.query(
        IncidentDB
    ).filter(
        IncidentDB.environment == "integration"
    ).count(),
    
    "Development incidents":db.query(
        IncidentDB
    ).filter(
        IncidentDB.environment == "development"
    ).count(),

    "Assigned incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.assigned_to.isnot(None)
    ).count(),

    "Unassigned incidents": db.query(
        IncidentDB
    ).filter(
        IncidentDB.assigned_to.is_(None)
    ).count(),
    }
def update_incident(
    incident_id: str,
    item_update,
    db: Session 
):

    incident = (
        db.query(IncidentDB)
        .filter(
            IncidentDB.incident_id == incident_id
        )
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail=f"Incident {incident_id} not found"
        )

    for field, value in item_update.model_dump(exclude_unset=True).items():
        setattr(incident, field, value)

    db.commit()

    db.refresh(incident)

    return incident

def delete_incident(
    incident_id: str,
    db: Session 
):

    incident = (
        db.query(IncidentDB)
        .filter(
            IncidentDB.incident_id == incident_id
        )
        .first()
    )

    if not incident:
        raise HTTPException(
            status_code=404,
            detail=f"Incident {incident_id} not found"
        )

    db.delete(incident)

    db.commit()

    return {
        "message": f"Incident {incident_id} deleted successfully"
    }

