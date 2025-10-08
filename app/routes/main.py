from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    return render_template('index.html')

@main_bp.route('/portfolio/<username>')
def portfolio(username):
    from app.models import User
    user = User.query.filter_by(username=username).first_or_404()
    skills = user.skills.all()
    projects = user.projects.all()
    return render_template('portfolio_public.html', user=user, skills=skills, projects=projects)
