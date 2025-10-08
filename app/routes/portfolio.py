from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from app.models import User
from datetime import datetime

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/<username>')
def portfolio(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('portfolio_public.html', user=user)

@portfolio_bp.route('/print/<username>')
@login_required
def print_portfolio(username):
    user = User.query.filter_by(username=username).first_or_404()
    
    if user != current_user and not current_user.is_admin:
        abort(403)
    
    return render_template(
        'portfolio_print.html',
        user=user,
        skills=user.skills.all(),
        projects=user.projects.all(),
        now=datetime.utcnow()
    )