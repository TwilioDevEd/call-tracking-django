<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Call Tracking (Django)

[![Build and test](https://github.com/TwilioDevEd/call-tracking-django/actions/workflows/build_test.yml/badge.svg)](https://github.com/TwilioDevEd/call-tracking-django/actions/workflows/build_test.yml)
[![Coverage Status](https://coveralls.io/repos/TwilioDevEd/call-tracking-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/TwilioDevEd/call-tracking-django?branch=master)

Use Twilio to track the effectiveness of your different marketing campaigns. Learn how call tracking helps organizations in [these Twilio customer stories](https://www.twilio.com/use-cases/call-tracking).

## Quickstart

### Create a TwiML App

This project is configured to use a **TwiML App**, which allows us to easily set the voice URLs for all Twilio phone numbers we purchase in this app.

Create a new TwiML app at https://www.twilio.com/user/account/apps/add and use its `Sid` as the `TWIML_APPLICATION_SID` environment variable wherever you run this app.

You can learn more about TwiML apps here: https://www.twilio.com/help/faq/twilio-client/how-do-i-create-a-twiml-app

### Twilio Account Settings

| Config&nbsp;Value | Description                                                                                                                                                  |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account&nbsp;Sid  | Your primary Twilio account identifier - find this [in the Console](https://www.twilio.com/console).                                                         |
| Auth&nbsp;Token   | Used to authenticate - [just like the above, you'll find this here](https://www.twilio.com/console).                                                         |
| TwiML app&nbsp;Sid | TwiML app SID created [here](https://www.twilio.com/user/account/apps/add) |

### Local development

This project is built using the [Django](https://www.djangoproject.com/) web framework. It runs on Python 3.6+.

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

1. Copy the `.env.example` file to `.env`, and edit it to include your Twilio API credentials (found at https://www.twilio.com/user/account/voice)

1. Run `source .env` to apply the environment variables (or even better, use [autoenv](https://github.com/kennethreitz/autoenv))

1. Run the migrations with:

    ```
    python manage.py migrate
    ```

1. Optionally create a superuser so you can access the Django admin:

    ```
    python manage.py createsuperuser
    ```

1. Collect static files from each of your application

    ```
    python manage.py collectstatic
    ```

1. Start the development server

    ```
    python manage.py runserver
    ```

To actually forward incoming calls, your development server will need to be publicly accessible. [We recommend using ngrok to solve this problem](https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html).

Once you have started ngrok, update your TwiML app's voice URL setting to use your ngrok hostname, so it will look something like this:

```
http://88b37ada.ngrok.io/call-tracking/forward-call
```

*Note:* To enable debug logs in local environment, set the `DEBUG` variable to `True` in the `local.py` file
### Use Production Environment

Follow previous guide and in step 6 do:

1. Copy the `.env.prod.example` file to `.env`, and edit it to include your Twilio API credentials (found at https://www.twilio.com/user/account/voice)
## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

```
$ coverage run manage.py test --settings=twilio_sample_project.settings.test
```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
