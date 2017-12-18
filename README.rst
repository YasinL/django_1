=====
django_app
=====

django_app is a simple Django app to conduct Web-based django_app. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_app',
    )

2. Include the django_app URLconf in your project urls.py like this::

    url(r'^django_app/', include('django_app.urls')),

3. Run `python manage.py migrate` to create the django_app models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/django_app/ to participate in the poll.