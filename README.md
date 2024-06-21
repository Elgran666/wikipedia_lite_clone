# Wikipedia Lite

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Running the Application](#running-the-application)



## Overview
This project is a simplified version of Wikipedia. The goal is to create a dynamic encyclopedia where users can search, read, create, and edit articles using Django. 
The project basically demonstrates basic CRUD (Create, Read, Update, Delete) operations, handling markdown content, and implementing search functionality.



## Project Structure 
Key files and directories:

manage.py: Django's command-line utility for administrative tasks.
wiki/: Main project directory containing core settings and configurations.
settings.py: Configuration settings for the Django project.
urls.py: URL declarations for the project.
encyclopedia/: Main app directory for the encyclopedia functionalities.
views.py: Contains the views for handling requests and responses.
urls.py: URL declarations specific to the encyclopedia app.
templates/encyclopedia/: Directory for HTML templates.
layout.html: Base template with common structure.
index.html: Template for the homepage listing all articles.
wiki.html: Template for displaying individual articles.
create_new_page.html: Template for creating new articles.
edit_page.html: Template for editing existing articles.
didyoumean.html: Template for search suggestions.
static/: Directory for static files like CSS and images.
util.py: Contains utility functions for interacting with markdown files.



## Running the Application
Having the following prerequisites:
- Python 3.x
- pip (Python package installer)


1. clone the repository: ```git clone```

2. then cd into it: ```cd```

3. install Django: ```pip install django```

4. run the Django server: ```python manage.py runserver```

5. open the browser and go to "http://127.0.0.1:8000"
