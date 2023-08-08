from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CreateJobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    salary = StringField('Salary', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    job_type = SelectField('Job Type', choices=[('', 'Select a Job Type'), ('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    email = StringField('Contact Email', validators=[DataRequired(), Email()])
    category = SelectField('Category', validators=[DataRequired()])
    submit = SubmitField('Create Job')
