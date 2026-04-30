# 🧠 Django Project Setup & Run Guide (All-in-One)

## 📦 Clone Project
git clone <repository-url>
cd <project-folder>

## 🐍 Virtual Environment

### macOS / Linux
python3 -m venv env
source env/bin/activate

### Windows
python -m venv env
env\Scripts\activate

## 📥 Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

## 🔐 Environment Variables (.env)
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

# SQLite
DATABASE_URL=sqlite:///db.sqlite3

# PostgreSQL (optional)
# DB_NAME=your_db
# DB_USER=your_user
# DB_PASSWORD=your_password
# DB_HOST=localhost
# DB_PORT=5432

## 🗄️ Database
python manage.py makemigrations
python manage.py migrate

## 👤 Create Superuser
python manage.py createsuperuser

## 📁 Static & Media

# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# collect static (production)
python manage.py collectstatic

## ▶️ Run Server
python manage.py runserver

http://127.0.0.1:8000/

## 🧪 Tests
python manage.py test

## 🛠️ Useful Commands
python manage.py startapp <app_name>
python manage.py shell
python manage.py showmigrations
python manage.py makemigrations <app_name>

## ⚠️ Troubleshooting

# Port issue
python manage.py runserver 8001

# Missing modules
pip install -r requirements.txt

# DB issues
python manage.py migrate

# Reset SQLite
rm db.sqlite3
python manage.py migrate

## 🔐 .gitignore
env/
__pycache__/
*.pyc
db.sqlite3
.env
staticfiles/
media/

## ✅ Best Practices
- Use virtual environments  
- Never commit .env  
- Use PostgreSQL in production  
- Keep apps modular (services/selectors pattern)

## 🚀 Production Notes
- Use gunicorn instead of runserver  
- Use nginx for static/media  
- Set DEBUG=False  

## ⚡ Quick Start
git clone <repo>
cd project
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
