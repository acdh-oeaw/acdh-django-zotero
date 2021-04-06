=============================
acdh-django-zotero
=============================

.. image:: https://badge.fury.io/py/acdh-django-zotero.svg
    :target: https://badge.fury.io/py/acdh-django-zotero


A django package to store/process zotero items

Documentation
-------------



Quickstart
----------

Install acdh-django-zotero::

    pip install acdh-django-zotero

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bib',
        ...
    )

Add following Zotero settings to you settings-file:

    .. code-block:: python

        Z_ID = "{a valid zotero API user ID}"
        Z_LIBRARY_TYPE = 'group' # or 'user'
        Z_API_KEY = "{a valid Zotero API user key}"
        Z_NN = {placeholder if no kind of creator is set, defaults to 'N.N.'}

See [pyzotero](http://pyzotero.readthedocs.io/en/latest/) for more information

Add acdh-django-zotero's URL patterns:

.. code-block:: python

    from rest_framework import routers

    ...
    from bib import urls as bib_urls
    from bib.api_views import ZotItemViewSet
    ...

    ...
    router = routers.DefaultRouter()
    router.register(r'zotitems', ZotItemViewSet)
    ...

    urlpatterns = [
        ...
        url(r'^bib/', include('bib.urls', namespace='bib')),
        ...
    ]

And run `python manage.py migrate`

Features
--------

* `bib` app registers a `ZotItem?  class which stores (some) information taken from a full zotero item entry. It provides then autocomplete functions for those ZotItem objects.
* The app also provides `management` commands to import items from a zotero library as well as to update existing items.

    `python manage.py bib_import --limit=15` # imports the top 15 items
    `python manage.py bib_import --since=100` # imports all items from library version 100
    `python manage.py bib_import` # import everything

    `python manage.py bib_update` # imports all items with a higher version number then the highest version number of the items stored in your db.

* The latter function can also be triggered through the front end by browsing to `{root}/bib/synczotero`

Build and publish
-----

.. code-block:: console

    python setup.py sdist bdist_wheel
    twine upload dist/*

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
