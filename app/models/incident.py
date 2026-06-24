from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Text,
    func
)

from app.database.base import Base



class Incident(Base):

    __tablename__ = "incidents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    incident_id = Column(
        String,
        unique=True
    )

    short_description = Column(
        String
    )

    description = Column(
        Text
    )

    criticality = Column(
        String
    )

    status = Column(
        String
    )
    reporter = Column(
        String
    )
    assigned_to = Column(
        String
    )
    service_name = Column(
        String
    )
    environment = Column(
        String
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()    
    )
    priority = Column(String)