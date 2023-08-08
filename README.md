# Career Hub

### Disclaimer
This has only been run on a linux machine, so it may not work on other operating systems.

### Installation
I have created a docker container that should work on any operating system.\
To run the docker container, run the following commands:
```bash
docker build -t careerhub .
docker run -p 5000:5000 -e FLASK_APP=app.py -e FLASK_ENV=development careerhub
```
Then go to http://localhost:5000/ in your browser.

## Overview

This is a job search website that allows users to search for jobs by type, salary, dates, categories and job title. Users can also create an account and post jobs.

## Contribute

Make sure you have Python 3.8 or above (and pip) installed.
Run the following commands to install the dependencies.

```bash
pip install -r requirements.txt
```

## Login Page

The splash page of the website is the latest jobs from all users. Users can also login or sign up.

![image]()

## Sign Up Page

The page where new users can register a new user into the database.

![image]()

## Home Page

This is the main page where users can view all the jobs posted by all users. Users can also search for jobs by title or company as well as sign up, login or logout.

![image]()

## Categories Page

This page allows users to search for jobs by category. They can also filter by salary, date posted and type or sort by newset, oldest, highest or lowest salary.

![image]()

## Search Page

This page allows users to search for jobs by title or company. They can also filter by salary, date posted and type or sort by newset, oldest, most or least money.

![image]()

# Challenges

-   Creating and validating users
-   Adding jobs
-   Only showing so many jobs per page
-   Filter and Sort
-   Searching and Categorizing

# Future Features

-   Link to company website
-   Post expire after companies list as fufilled
-   Link post to user
-   Allow users to edit posts
-   Filter by location
-   Allow users to upload resumes
-   Allow users to upload profile pictures
