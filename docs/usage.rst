=====
Usage
=====

To use acdh-django-zotero in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bib.apps.BibConfig',
        ...
    )

Add acdh-django-zotero's URL patterns:

.. code-block:: python

    from bib import urls as bib_urls


    urlpatterns = [
        ...
        url(r'^', include(bib_urls)),
        ...
    ]
