import os

from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "development")
app.run(port=int(os.getenv("PORT")) or 5000)
