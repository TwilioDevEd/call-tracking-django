# Call Tracking (Django)

[![Build Status](https://travis-ci.org/TwilioDevEd/call-tracking-django.svg?branch=master)](https://travis-ci.org/TwilioDevEd/call-tracking-django)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/call-tracking-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/TwilioDevEd/call-tracking-django?branch=master)

Use Twilio to track the effectiveness of your different marketing campaigns. Learn how call tracking helps organizations in [these Twilio customer stories](https://www.twilio.com/use-cases/call-tracking).

## Quickstart

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/user/account/apps/add and use its `Sid` as the `TWILIO_APPLICATION_SID` environment variable wherever you run this app.

You can learn more about TwiML apps here: https://www.twilio.com/help/faq/twilio-client/how-do-i-create-a-twiml-app

### Heroku

The easiest way to run this app is by deploying it to [Heroku](https://www.heroku.com/). You can run this app for free in minutes:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/call-tracking-django)

After your app deploys, you will need to update your TwiML app to use the Heroku server's hostname in the TwiML app's voice URL field. It will look something like this:

```
http://young-journey-3547.herokuapp.com/call-tracking/forward-call
```

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

To actually forward incoming calls, your development server will need to be publicly accessible. [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html).

Once you have started ngrok, update your TwiML app's voice URL setting to use your ngrok hostname, so it will look something like this:

```
http://88b37ada.ngrok.io/call-tracking/forward-call
```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

```
$ coverage run manage.py test --settings=twilio_sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
