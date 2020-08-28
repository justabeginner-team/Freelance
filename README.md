# Freelance  [![Build Status](https://travis-ci.org/justabeginner-team/Freelance.svg?branch=master)](https://travis-ci.org/justabeginner-team/Freelance)

This project is built using the [Django](https://www.djangoproject.com/) web framework. 
It runs on Python 3.7+ and uses templates from [MDB-Ecommerce templates](https://mdbootstrap.com/)

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/), run `virtualenv venv` and then `source venv/bin/activate`
    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), run `mkvirtualenv venv`
1. Install the requirements with `pip install -r requirements.txt`

1. Run the migrations with `python manage.py migrate`
1. Optionally create a superuser so you can access the Django admin: `python manage.py createsuperuser`
1. Copy the `.env.example` file to `.env`,  and fill in the environment specifics
1. Run the server with `python manage.py runserver`
