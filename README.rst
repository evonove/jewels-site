==============
Jewels website
==============

`jewels.game`_ website, made with `Wagtail`_!

.. _jewels.game: https://jewels.game/
.. _Wagtail: https://wagtail.io/


Getting started
---------------

Running this website requires the following backend services up and running:

* Redis
* PostgreSQL

If your database is running via ``docker-compose`` and the binding *address:port* is exposed to
the host, you should execute the commands below so that a default user and database are created. Just:

.. code-block:: bash

    $ docker exec -ti jewelssite_db_1 su -c "createuser devel -P --createdb" postgres
    $ docker exec -ti jewelssite_db_1 su -c "createdb jewels -O devel" postgres

Populate the database
~~~~~~~~~~~~~~~~~~~~~

From the ``django-website`` folder, launch:

.. code-block:: bash

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver

Settings
--------

``jewels`` requires the following settings in order to work as expected.

These environment variables must be set when using the ``production.py`` settings; this may not be
necessary while in development or testing mode, and no SSL connection will be used.

Django
~~~~~~

* ``DJANGO_SECRET_KEY`` (default: ``None``)
* ``DJANGO_SETTINGS_MODULE`` (default: ``None``)
* ``DJANGO_ALLOWED_HOSTS`` (default: ``None``)
* ``DJANGO_ASSETS_ROOT`` (default: project root folder)
* ``DJANGO_SECURE_SSL_REDIRECT`` (default: ``True``)
* ``DJANGO_SESSION_COOKIE_SECURE`` (default: ``True``)

Backends
~~~~~~~~

These environment variables define the service connection strings. You may set
these values according to your development environment. If you are using ``docker``,
just change ``DATABASE_URL`` and ``CACHE_URL`` with your linked container URLs.

* ``DATABASE_URL`` (default: ``postgres://devel:123456@127.0.0.1:5432/jewels``)
* ``CACHE_URL`` (default: ``redis://127.0.0.1:6379/1``)

Email
~~~~~

* ``DJANGO_EMAIL_BACKEND`` (default: ``django.core.mail.backends.smtp.EmailBackend``)
* ``DJANGO_FROM_EMAIL`` (default: ``None``)
* ``DJANGO_EMAIL_HOST`` (default: ``None``)
* ``DJANGO_EMAIL_HOST_PORT`` (default: ``None``)
* ``DJANGO_EMAIL_HOST_USER`` (default: ``None``)
* ``DJANGO_EMAIL_HOST_PASSWORD`` (default: ``None``)
* ``DJANGO_EMAIL_USE_TLS`` (default: ``True``)

Application server
~~~~~~~~~~~~~~~~~~

* ``UWSGI_HTTP``: sets the binding *address:port*
* ``UWSGI_SOCKET``: sets the unix socket path
* ``UWSGI_PROCESSES``: sets the number of uWSGI processes

Logging and monitoring
~~~~~~~~~~~~~~~~~~~~~~

* ``LOGSTASH_HOST`` (default: ``127.0.0.1``)
* ``LOGSTASH_PORT`` (default: ``5000``)
* ``NEW_RELIC_CONFIG_FILE``: sets the NewRelic configuration file ``newrelic.ini``
* ``SENTRY_DSN``: sets the ``DSN`` value, found in the Sentry setup page

Running on production
---------------------

The service may be wrapped using NewRelic. In this case, launch the application server with the
following command:

.. code-block:: bash

    $ newrelic-admin run-program uwsgi
