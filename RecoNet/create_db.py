# create_db.py
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    try:
        db.create_all()
        print("Database created .......")
    except Exception as e:
        print(f"Error creating database: {e}")