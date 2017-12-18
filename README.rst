=====
django_all
=====

django_all is a simple Django app to conduct Web-based django_all. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_all" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_all',
    )

2. Include the django_all URLconf in your project urls.py like this::

    url(r'^django_all/', include('django_all.urls')),

3. Run `python manage.py migrate` to create the django_all models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/django_all/ to participate in the poll.