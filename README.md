# Django Project Setup & Run Guide

## 1. Clone & enter

```bash
git clone <repository-url>
cd <project-folder>
```

---

## 2. Virtual environment

**macOS / Linux**
```bash
python3 -m venv env
source env/bin/activate
```

**Windows**
```bash
python -m venv env
env\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Environment variables (`.env`)

```env
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

# SQLite (default)
DATABASE_URL=sqlite:///db.sqlite3

# PostgreSQL (production)
# DB_NAME=your_db
# DB_USER=your_user
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432
```

---

## 5. Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 6. Static & media

Add to `settings.py`:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Collect static files before deploying:

```bash
python manage.py collectstatic
```

---

## 7. Run server

```bash
python manage.py runserver
# → http://127.0.0.1:8000/
```

---

## 8. Run tests

```bash
python manage.py test
```

---

## 9. Useful commands

```bash
python manage.py startapp <app_name>   # create a new app
python manage.py shell                 # open Django shell
python manage.py showmigrations        # list all migrations
python manage.py makemigrations <app>  # migrate a specific app
```

---

## 10. Troubleshooting

```bash
# Port conflict
python manage.py runserver 8001

# Missing modules
pip install -r requirements.txt

# DB issues
python manage.py migrate

# Reset SQLite
rm db.sqlite3
python manage.py migrate
```

---

## 11. `.gitignore` essentials

```
env/
__pycache__/
*.pyc
db.sqlite3
.env
staticfiles/
media/
```

---

## 12. Best practices

- Always use virtual environments
- Never commit `.env` to version control
- Use PostgreSQL in production
- Keep apps modular — services/selectors pattern

---

## 13. Production notes

- Use **gunicorn** instead of `runserver`
- Use **Nginx** to serve static and media files
- Set `DEBUG=False`

---

## Quick start

```bash
git clone <repo>
cd project
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
