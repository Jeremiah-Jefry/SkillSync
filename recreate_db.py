from app import create_app, db
from app.models import User, Skill, Project

def recreate_db():
    app = create_app()
    with app.app_context():
        # Drop all tables
        db.drop_all()
        print("Dropped all tables")
        
        # Create all tables
        db.create_all()
        print("Created all tables")

if __name__ == '__main__':
    recreate_db()