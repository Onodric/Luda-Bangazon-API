# Bangazon API

An API supplied for the developers at Bangazon, LLC. Used to expose relevant database resources for view, creation, edit, or deletion.

## Steps to Install

The API uses the Django framework, running on Python 3.6

To install the project locally:

1. Set up [Python 3.6](https://www.python.org/) on your machine per the install instructions
1. Install [pip](https://pip.pypa.io/en/stable/installing/)
1. Install Django 1.10.5 via pip: `pip install django`
1. Clone the repository to desired location
1. Migrate the database tables. In the main project directory `~/Luda-Bangazon-API/Bangazon` (where `manage.py` is located), run the command `python manage.py migrate`
1. Start the development server. Run the command `python manage.py runserver`. Take note of the IP address and host port given.
1. Start a browser, and navigate to the IP and port,  followed by `/api/`. i.e. ```127.0.0.1:8000/api/```. Other resources may be reached from `admin` and `api_auth`.


## Installed Dependencies 

The API relies upon the following dependencies:

1. Python >v.3.6
1. Django >v1.10.5

## System Config

The API should run on all systems that meet the dependency requirements.
