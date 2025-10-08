from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, ValidationError, Optional
from flask_wtf.file import FileField, FileAllowed
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    bio = TextAreaField('Bio', validators=[Optional(), Length(max=500)])
    profile_picture = FileField('Profile Picture', validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    github_username = StringField('GitHub Username', validators=[Optional(), Length(max=100)])
    linkedin_url = StringField('LinkedIn Profile', validators=[Optional(), Length(max=255)])
    portfolio_url = StringField('Portfolio Website', validators=[Optional(), Length(max=255)])

class SkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired(), Length(max=100)])
    category = SelectField('Primary Category', validators=[DataRequired()], choices=[
        ('programming_languages', 'Programming Languages'),
        ('web_technologies', 'Web Technologies'),
        ('frameworks_libraries', 'Frameworks & Libraries'),
        ('databases', 'Databases & Storage'),
        ('cloud_services', 'Cloud Services'),
        ('devops_tools', 'DevOps & Tools'),
        ('mobile_development', 'Mobile Development'),
        ('design_multimedia', 'Design & Multimedia'),
        ('ai_ml', 'AI & Machine Learning'),
        ('security', 'Security & Authentication'),
        ('soft_skills', 'Soft Skills'),
        ('other', 'Other')])
    subcategory = StringField('Subcategory', validators=[Optional(), Length(max=50)])
    level = IntegerField('Skill Level (0-10)', validators=[
        DataRequired(),
        NumberRange(min=0, max=10, message='Level must be between 0 and 10')])
    description = TextAreaField('Description', validators=[Optional(), Length(max=500)])
    tags = StringField('Tags (comma-separated)', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Save Skill')

class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired(), Length(max=150)])
    description = TextAreaField('Description', validators=[DataRequired()])
    tech_stack = StringField('Technologies (comma-separated)', validators=[Optional(), Length(max=255)])
    github_url = StringField('GitHub URL', validators=[Optional(), Length(max=255)])
    demo_url = StringField('Demo URL', validators=[Optional(), Length(max=255)])
    image_url = StringField('Image URL', validators=[Optional(), Length(max=255)])
    status = SelectField('Status', choices=[
        ('completed', 'Completed'),
        ('in-progress', 'In Progress'),
        ('planned', 'Planned')
    ], default='completed')
    submit = SubmitField('Save Project')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


