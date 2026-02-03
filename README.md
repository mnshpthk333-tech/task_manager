# Task Manager API

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`

## API Endpoints
- `POST /api/users/` - Register
- `POST /api/token/` - Obtain JWT token
- `GET /api/tasks/` - List tasks
- `POST /api/tasks/` - Create task
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task
- `GET /swagger/` - API documentation

## Tests
```bash
python manage.py test

---

This setup satisfies **all your core requirements**, including CRUD, JWT auth, Swagger docs, and unit tests. Pagination, filtering, and roles are optional enhancements.  

---


