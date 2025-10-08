from app import create_app, db
from app.models import User, Skill, Project
from sqlalchemy import text

app = create_app()

def upgrade_database():
    with app.app_context():
        # Add profile_picture column if it doesn't exist
        try:
            db.session.execute(text('ALTER TABLE user ADD COLUMN profile_picture TEXT DEFAULT "default_profile.png"'))
            db.session.commit()
            print("Added profile_picture column successfully")
        except Exception as e:
            print(f"Error adding column (might already exist): {e}")
            db.session.rollback()

        # Add subcategory and tags columns to skills if they don't exist
        try:
            db.session.execute(text('ALTER TABLE skill ADD COLUMN subcategory TEXT'))
            db.session.execute(text('ALTER TABLE skill ADD COLUMN tags TEXT'))
            db.session.execute(text('ALTER TABLE skill ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP'))
            db.session.execute(text('ALTER TABLE skill ADD COLUMN last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP'))
            db.session.commit()
            print("Added subcategory and tags columns successfully")
        except Exception as e:
            print(f"Error adding columns (might already exist): {e}")
            db.session.rollback()

if __name__ == '__main__':
    upgrade_database()