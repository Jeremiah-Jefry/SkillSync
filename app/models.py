from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text)
    github_username = db.Column(db.String(100))
    linkedin_url = db.Column(db.String(255))
    portfolio_url = db.Column(db.String(255))
    profile_picture = db.Column(db.String(255), default='default_profile.png')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    skills = db.relationship('Skill', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    projects = db.relationship('Project', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_skill_count(self):
        return self.skills.count()
    
    def get_project_count(self):
        return self.projects.count()
    
    def get_average_skill_level(self):
        skills = self.skills.all()
        if not skills:
            return 0
        return sum([skill.level for skill in skills]) / len(skills)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50))
    level = db.Column(db.Integer, nullable=False)  # 0-10 scale
    description = db.Column(db.Text)
    tags = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_tags_list(self):
        return [tag.strip() for tag in (self.tags or '').split(',') if tag.strip()]
    
    def __repr__(self):
        return f'<Skill {self.name}: {self.level}/10>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    tech_stack = db.Column(db.String(255))  # Comma-separated technologies
    github_url = db.Column(db.String(255))
    demo_url = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    status = db.Column(db.String(20), default='completed')  # completed, in-progress, planned
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def get_tech_stack_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')] if self.tech_stack else []
    
    def __repr__(self):
        return f'<Project {self.title}>'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
