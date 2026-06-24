from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IncidentCreate(BaseModel):
    short_description: str
    description: str
    criticality: str
    status: str = "open"
    reporter: str
    assigned_to: Optional[str] = None
    service_name: str
    environment: str
    #created_at: Optional[datetime] = None


class IncidentUpdate(BaseModel):
    short_description: Optional[str] = None
    description: Optional[str] = None
    criticality: Optional[str] = None
    status: Optional[str] = None
    reporter: Optional[str] = None
    assigned_to: Optional[str] = None
    service_name: Optional[str] = None
    environment: Optional[str] = None    


class IncidentResponse(IncidentCreate):
    id: int
    incident_id: str
    created_at: datetime

    class Config:
        from_attributes = True