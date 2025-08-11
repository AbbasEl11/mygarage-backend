# 🛠️ MyGarage Backend (Django REST API)

This is the backend for the **MyGarage** app. It exposes a REST API for managing vehicles and related data.
The frontend (Ionic + React) consumes these endpoints.

➡ **Backend Repository:** [MyGarage Frontend](https://github.com/AbbasEl11/mygarage-app) 

---

## ✨ Features

- Django + Django REST Framework
- CRUD for cars (create / list / retrieve / update / delete)
- Optional image upload endpoints (if enabled)
- CORS configured for local development
- SQLite by default, easy to switch to Postgres/MySQL

---

## 🚀 Quickstart

```bash
# Clone & enter
git clone https://github.com/AbbasEl11/mygarage-backend.git
cd mygarage-backend

# Create virtual env
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

# Install deps
pip install -r requirements.txt

# Migrate & run
python manage.py migrate
python manage.py runserver
```

The API will be available at: http://127.0.0.1:8000/

---

## 🔌 API Endpoints (example)

Assuming a `CarViewSet` is registered on `cars`:

```
GET    /cars/           # list
POST   /cars/           # create
GET    /cars/{id}/      # retrieve
PUT    /cars/{id}/      # update (full)
PATCH  /cars/{id}/      # update (partial)
DELETE /cars/{id}/      # delete
```

> Your frontend should call `DELETE /cars/{id}/` (no request body) and expect `204 No Content` on success.

If you have an image upload route (example):
```
POST /cars/{id}/upload-images/  # multipart/form-data
```

---

## 🌐 CORS (local dev)

In `settings.py` make sure CORS is enabled and your frontend origin is allowed:

```python
INSTALLED_APPS += ['corsheaders', 'rest_framework']

MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware', *MIDDLEWARE]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vite (Ionic React)
    # "https://your-frontend-domain.tld",
]
```

---

## 🧰 Environment

- `DEBUG=True` for development only
- Do **not** commit secrets. Load them from environment variables or a `.env` file (not committed).

---

## 📦 Dependencies

See `requirements.txt`. Minimal set:

- Django
- djangorestframework
- django-cors-headers
- (Optional) Pillow for image uploads
- (Optional) drf-spectacular for API docs

---

## 📚 API Docs (optional)

If you want OpenAPI/Swagger docs, add **drf-spectacular**:

```python
# settings.py
INSTALLED_APPS += ["drf_spectacular"]
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
```

```python
# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
```

Then open: `/api/docs/`

---

## 🗃️ Project Structure (recommended)

```
mygarage-backend/
├─ mysite/
│  ├─ settings.py
│  ├─ urls.py
│  └─ __init__.py
├─ garage/
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  ├─ migrations/
│  └─ __init__.py
├─ manage.py
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

## ✅ Before committing

- Remove `venv/` and `db.sqlite3` from the repo if present
- Ensure `.gitignore` includes `venv/`, `db.sqlite3`, `__pycache__/`, `.env`
- Run migrations successfully
- Test CRUD via `curl` or your frontend

---

## Author
Developed by [AbbasEl11](https://https://github.com/AbbasEl11)


