# Call Tracking (Django)

[![Build Status](https://travis-ci.org/TwilioDevEd/call-tracking-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/call-tracking-django)

Use Twilio to track how many calls different marketing leads receive.

## Quickstart

### Heroku

This project is preconfigured to run on [Heroku](https://www.heroku.com/). Deploy it now:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/call-tracking-django)

### Local development

This project is built using the [Django](https://www.djangoproject.com/) web framework. It runs on Python 2.7+ and Python 3.4+.

To run the app locally, first clone this repository and `cd` into its directory. Then:

1. Create a new virtual environment:
    - If using vanilla [virtualenv](https://virtualenv.pypa.io/en/latest/):

        ```
        virtualenv venv
        source venv/bin/activate
        ```

    - If using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/):

        ```
        mkvirtualenv call-tracking
        ```

1. Install the requirements:

    ```
    pip install -r requirements.txt
    ```

1. Start a local PostgreSQL database and create a database called `call_tracking`:
    - If on a Mac, I recommend [Postgres.app](http://postgresapp.com/). After install, open psql and run `CREATE DATABASE call_tracking;`
    - If Postgres is already installed locally, you can just run `createdb call_tracking` from a terminal
1. Run the migrations with:

    ```
    python manage.py migrate
    ```

1. Optionally create a superuser so you can access the Django admin:

    ```
    python manage.py createsuperuser
    ```

1. Copy the `.env_example` file to `.env`, and edit it to include your Twilio API credentials (found at https://www.twilio.com/user/account/voice)
1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))
1. Start the development server

    ```
    python manage.py runserver
    ```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/en/coverage-3.7.1/#):

```
$ coverage run manage.py test --settings=sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
