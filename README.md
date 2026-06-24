# Incident Management Platform

A backend application designed for incident lifecycle management, built to simulate a production-style internal platform used for tracking, updating, and managing operational incidents.

This project focuses on backend architecture, API design, containerization, database management, and infrastructure practices.

---

## Features

### Incident Management

* Create incidents
* Retrieve all incidents
* Retrieve incident by business ID
* Update incident details
* Delete incidents

### Dashboard & Analytics

* Total incidents overview
* Open incidents count
* Resolved incidents count
* Critical incidents overview
* Environment-based statistics
* Assignment statistics

### Database

* PostgreSQL integration
* SQLAlchemy ORM
* Persistent storage
* Database schema versioning with Alembic

### Infrastructure

* Dockerized application
* Docker Compose orchestration
* Environment-based configuration
* Layered backend architecture

---

## Tech Stack

| Category              | Technology |
| --------------------- | ---------- |
| Language              | Python     |
| API Framework         | FastAPI    |
| Database              | PostgreSQL |
| ORM                   | SQLAlchemy |
| Containerization      | Docker     |
| Database Migration    | Alembic    |
| API Docs              | Swagger UI |
| Dependency Management | pip        |

---

## Architecture

The application follows a layered architecture pattern:

```text
Client
   ↓
Router Layer
   ↓
Service Layer
   ↓
Database Layer
   ↓
PostgreSQL
```

Project structure:

```text
app/
├── database/
│   ├── base.py
│   └── database.py
│
├── models/
│   └── incident.py
│
├── routers/
│   └── incidents.py
│
├── schemas/
│   └── incident.py
│
├── services/
│   └── incident_service.py
│
├── main.py

migrations/
Dockerfile
docker-compose.yml
requirements.txt
```

---

## API Endpoints

### Incidents

| Method | Endpoint               | Description       |
| ------ | ---------------------- | ----------------- |
| POST   | `/items`               | Create incident   |
| GET    | `/items`               | Get all incidents |
| GET    | `/items/{incident_id}` | Get incident      |
| PUT    | `/items/{incident_id}` | Update incident   |
| DELETE | `/items/{incident_id}` | Delete incident   |

### Dashboard

| Method | Endpoint           |
| ------ | ------------------ |
| GET    | `/items/dashboard` |

---

## Running Locally

### Clone repository

```bash
git clone <repository-url>
cd incident-management-platform
```

### Build and start

```bash
docker compose up --build
```

Application:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Database Migrations

Generate migration:

```bash
alembic revision --autogenerate -m "migration_name"
```

Apply migration:

```bash
alembic upgrade head
```

---

## Example Request

Create incident:

```json
{
  "short_description": "API latency increase",
  "description": "Response time increased above threshold",
  "criticality": "high",
  "status": "open",
  "reporter": "operations-team",
  "assigned_to": "backend-team",
  "service_name": "incident-api",
  "environment": "production"
}
```

---

## Future Improvements

* Authentication and authorization
* Automated testing
* CI/CD pipeline
* GitHub Actions
* Kubernetes deployment
* Terraform provisioning
* Monitoring and observability

---

## Learning Goals

This project was built to practice:

* API development
* Backend architecture
* Containerization
* Database migrations
* Service separation
* Infrastructure concepts
* GitHub Actions
* CI/CD pipeline
---
