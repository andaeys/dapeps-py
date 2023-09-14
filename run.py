import time

from app import app, db
from app.models import User

# Initialize database
with app.app_context():
    try:
        time.sleep(1)
        db.create_all()
        print("anda_db Tables created successfully")
    except Exception as e:
        print(f"anda_db Error creating tables: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
