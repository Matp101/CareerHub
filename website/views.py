'''
views.py
How different pages are viewed by different users
'''
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import User, JobCategory, JobListing
from .forms import CreateJobForm
from . import db
import json
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote


views = Blueprint('views', __name__)

PAGE_SIZE = 10

def sort_by(sort):
    if sort == 'newest':
        return JobListing.date_posted.desc()
    elif sort == 'oldest':
        return JobListing.date_posted.asc()
    elif sort == 'most_money':
        return JobListing.salary.desc()
    elif sort == 'least_money':
        return JobListing.salary.asc()
    else:
        return JobListing.date_posted.desc()
    
def get_filters():
    min_salary = int(request.args.get('min_salary')) if request.args.get('min_salary') and request.args.get('min_salary') != 'None' else None
    max_salary = int(request.args.get('max_salary')) if request.args.get('max_salary') and request.args.get('max_salary') != 'None' else None
    posted_after = request.args.get('posted_after') if request.args.get('posted_after') and request.args.get('posted_after') != 'None' else None
    posted_before = request.args.get('posted_before') if request.args.get('posted_before') and request.args.get('posted_before') != 'None' else None
    job_type_filter = request.args.get('job_type_filter') if request.args.get('job_type_filter') and request.args.get('job_type_filter') != 'None' else None
    filters = {
        'min_salary': min_salary,
        'max_salary': max_salary,
        'posted_after': posted_after,
        'posted_before': posted_before,
        'job_type_filter': job_type_filter
    }
    return filters


def filter_results(query, filters):
    if filters['min_salary']:
        query = query.filter(JobListing.salary >= filters['min_salary'])
    if filters['max_salary']:
        query = query.filter(JobListing.salary <= filters['max_salary'])
    if filters['posted_after']:
        query = query.filter(JobListing.date_posted >= filters['posted_after'])
    if filters['posted_before']:
        query = query.filter(JobListing.date_posted <= filters['posted_before'])
    if filters['job_type_filter']:
        query = query.filter(JobListing.type == filters['job_type_filter'])
    return query

def add_email_syntax(job_listings):
    # Add the emailtitle attribute to job_listings
    if job_listings == None:
    	return None
    for job in job_listings.items:
        job.emailtitle = quote(job.title)
        job.emailcompany = quote(job.company)

@views.route('/', methods=['GET', 'POST'])
# @login_required  # Must be logged in to view
def home():
    users = User.query.all()
    
    page = request.args.get('page', 1, type=int)
    # Retrieve all users from the database
    jobs = JobListing.query.all()
    per_page = PAGE_SIZE
    job_listings = JobListing.query.order_by(JobListing.date_posted.desc()).paginate(page=page, per_page=per_page)
    
    filters = get_filters()
    add_email_syntax(job_listings)

    return render_template("home.html", user=current_user, users=users, job_listings=job_listings, filters=filters)


@views.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').strip()
    page = request.args.get('page', 1, type=int)
    per_page = PAGE_SIZE
    sort_criteria = request.args.get('sort', 'newest')
    sort = sort_by(sort_criteria)
    filters = get_filters()
    search_results = JobListing.query.filter(
        JobListing.title.contains(query) | 
        JobListing.company.contains(query))
    
    search_results = filter_results(search_results, filters).order_by(sort).paginate(page=page, per_page=per_page)
    if search_results.total == 0:
        search_results = None

    add_email_syntax(search_results)
    return render_template("search_results.html", query=query, search_results=search_results, user=current_user, sort=sort_criteria, filters=filters)

@views.route('/categories', methods=['GET', 'POST'])
def categories():
    categories = JobCategory.query.all()
    page = request.args.get('page', 1, type=int)
    per_page = PAGE_SIZE
    sort_criteria = request.args.get('sort', 'newest')
    sort = sort_by(sort_criteria)

    selected_category_id = request.args.get('category')
    if selected_category_id == 'None':
        selected_category_id = None
    selected_category_name = None

    if selected_category_id:
        selected_category = JobCategory.query.get(selected_category_id)
        if selected_category:
            selected_category_name = selected_category.category_name
    if selected_category_id:
        job_listings = JobListing.query.filter_by(category_id=selected_category_id)
    else:
        job_listings = JobListing.query

    filters = get_filters()
    job_listings = filter_results(job_listings, filters).order_by(sort).paginate(page=page, per_page=per_page)
    add_email_syntax(job_listings)
    return render_template("categories.html", user=current_user, categories=categories, job_listings=job_listings, selected_category=selected_category_id, selected_category_name=selected_category_name, sort=sort_criteria, filters=filters)

@views.route('/createjob', methods=['GET', 'POST'])
@login_required
def createjob():
    form = CreateJobForm()
    form.category.choices = [('', 'Select a Category')] 
    form.category.choices += [(category.category_id, category.category_name) for category in JobCategory.query.all()]

    if form.validate_on_submit():
        title = form.title.data
        company = form.company.data
        salary = form.salary.data
        location = form.location.data
        job_type = form.job_type.data
        description = form.description.data
        email = form.email.data
        category_id = form.category.data

        job_listing = JobListing(title=title, company=company, salary=salary, location=location, type=job_type, description=description, email=email, category_id=category_id)
        db.session.add(job_listing)
        db.session.commit()

        flash('Job listing created successfully!', 'success')
        return redirect(url_for('views.search'))

    return render_template("createjob.html", user=current_user, form=form)

@views.route('/job_listings', methods=['GET'])
def job_listings():
    job_listings = JobListing.query.all()
    return render_template("job_listings.html", job_listings=job_listings)

