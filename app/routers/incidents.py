from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.incident import IncidentCreate, IncidentUpdate, IncidentResponse

from app.services.incident_service import (
    create_incident, 
    get_incidents, 
    get_incident_by_id, 
    get_dashboard,
    update_incident,
    delete_incident)



router = APIRouter(
    prefix = "/items",
    tags = ["Incidents"]
)

#New post to database
@router.post("/",response_model=IncidentResponse)

def create_item(
    item: IncidentCreate,
    db: Session = Depends(get_db)
):

    return create_incident(
        db = db,
        item = item
    )

#New get from database
@router.get("/")
def list_items(
    limit: int = 10,
    offset: int = 0,
    status: str | None = None,
    criticality: str | None = None,
    assigned_to: str | None = None,
    db: Session = Depends(get_db)
):
    return get_incidents(
        db = db,
        limit = limit,
        offset = offset,
        status = status,
        criticality = criticality,
        assigned_to = assigned_to
    )


#Dashboard
@router.get("/dashboard")
def dashboard(
    db:Session = Depends(get_db)
):
    return get_dashboard(
        db = db
    )


#New get by incident_id from database
@router.get("/{incident_id}")
def get_item(
    incident_id: str,
    db: Session = Depends(get_db)
):
    return get_incident_by_id(
        db = db,
        incident_id = incident_id
    )

#New update in database 
@router.put("/{incident_id}")
def update_item(
    incident_id: str,
    item_update: IncidentUpdate,
    db:Session = Depends(get_db)
):
    return update_incident(
        db = db,
        incident_id = incident_id,
        item_update = item_update
    )


#New Delete from database
@router.delete("/{incident_id}")
def delete_item(
    incident_id:str,
    db:Session = Depends(get_db)
):
    return delete_incident(
        db = db,
        incident_id = incident_id
    )


#Old post 
""" 
@app.post("/items")
def create_item(item: Item):
        db_id = len(items) + 1
        item.incident_id = f"INC{db_id:06d}"
        items.append(item)
        return {"message": "Item created successfully", "item": items}
"""
#Old get
""" 
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10, offset: int = 0):
    return items[offset:offset+limit]
"""
#Old update
""" 
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
     items[item_id] = item
     return{"incident_id":items[item_id].incident_id ,"short_description":item.short_description, "description":item.description, "criticality":item.criticality, "status":item.status, "reporter":item.reporter, "assigned_to":item.assigned_to, "service_name":item.service_name, "environment":item.environment, "created_at":items[item_id].created_at}
"""
#Old get
""" 
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int) -> Item:
      if item_id < 0 or item_id >=len(items):
          raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
      else:
          return items[item_id]
""" 
#Old delete
""" 
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    
    deleted_item = items.pop(item_id)
    return {
        "message": f"Incident {deleted_item.incident_id} was deleted successfully",
        "incident_id": deleted_item.incident_id
    }
""" 