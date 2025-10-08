import os
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app import db
from app.models import User, Skill, Project
from app.forms import SkillForm, ProjectForm, ProfileForm

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def dashboard():
    skills_count = current_user.get_skill_count()
    projects_count = current_user.get_project_count()
    avg_skill_level = current_user.get_average_skill_level()
    
    recent_skills = current_user.skills.order_by(Skill.created_at.desc()).limit(5).all()
    recent_projects = current_user.projects.order_by(Project.created_at.desc()).limit(3).all()
    
    return render_template('dashboard/dashboard.html',
                         skills_count=skills_count,
                         projects_count=projects_count,
                         avg_skill_level=avg_skill_level,
                         recent_skills=recent_skills,
                         recent_projects=recent_projects)

@dashboard_bp.route('/skills')
@login_required
def skills():
    page = request.args.get('page', 1, type=int)
    skills = current_user.skills.paginate(
        page=page, per_page=20, error_out=False)
    return render_template('dashboard/skills.html', skills=skills)

@dashboard_bp.route('/add_skill', methods=['GET', 'POST'])
@login_required
def add_skill():
    form = SkillForm()
    if form.validate_on_submit():
        skill = Skill(
            name=form.name.data,
            category=form.category.data,
            subcategory=form.subcategory.data,
            level=form.level.data,
            description=form.description.data,
            tags=form.tags.data,
            user=current_user
        )
        db.session.add(skill)
        db.session.commit()
        flash('Skill added successfully!', 'success')
        return redirect(url_for('dashboard.skills'))
    
    return render_template('dashboard/add_skill.html', form=form)

@dashboard_bp.route('/projects')
@login_required
def projects():
    page = request.args.get('page', 1, type=int)
    projects = current_user.projects.paginate(
        page=page, per_page=10, error_out=False)
    return render_template('dashboard/projects.html', projects=projects)

@dashboard_bp.route('/add_project', methods=['GET', 'POST'])
@login_required
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            tech_stack=form.tech_stack.data,
            github_url=form.github_url.data,
            demo_url=form.demo_url.data,
            image_url=form.image_url.data,
            status=form.status.data,
            user=current_user
        )
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('dashboard.projects'))
    
    return render_template('dashboard/add_project.html', form=form)

def save_profile_picture(form_picture):
    # Generate a secure filename
    filename = secure_filename(form_picture.filename)
    # Create a unique filename with timestamp
    _, ext = os.path.splitext(filename)
    new_filename = f"profile_{current_user.id}{ext}"
    # Save the file
    filepath = os.path.join(current_app.root_path, 'static/uploads', new_filename)
    form_picture.save(filepath)
    return f'uploads/{new_filename}'

@dashboard_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.bio = form.bio.data
        current_user.github_username = form.github_username.data
        current_user.linkedin_url = form.linkedin_url.data
        current_user.portfolio_url = form.portfolio_url.data
        
        if form.profile_picture.data:
            try:
                picture_file = save_profile_picture(form.profile_picture.data)
                current_user.profile_picture = picture_file
            except Exception as e:
                flash('Error saving profile picture. Please try again.', 'danger')
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard.profile'))
    
    # Pre-populate form with current user data
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.bio.data = current_user.bio
    form.github_username.data = current_user.github_username
    form.linkedin_url.data = current_user.linkedin_url
    form.portfolio_url.data = current_user.portfolio_url
    
    return render_template('dashboard/profile.html', form=form)

@dashboard_bp.route('/api/skills_data')
@login_required
def skills_data():
    """API endpoint for skills chart data"""
    skills = current_user.skills.all()
    categories = {}
    levels = {}
    
    for skill in skills:
        if skill.category not in categories:
            categories[skill.category] = 0
        categories[skill.category] += 1
        
        if skill.level not in levels:
            levels[skill.level] = 0
        levels[skill.level] += 1
    
    return jsonify({
        'categories': categories,
        'levels': levels
    })
