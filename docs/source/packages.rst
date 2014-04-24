"Required" Packages
=========================

While none of this package actually requires any dependencies, the ones that I use most frequently are included.


Packages
-------------------------

The latest versions are installed from pypi, unless otherwise noted.

django:
    mvc (or mvt) platform. it rocks.

pillow:
    a fork of PIL (python imaging library) wich is now the latest, support version

south:
    schema and date migration tool for changes to django models

Sphinx:
    documentation generating based embedded comments in code as well as restructured text files

boto:
    a comprehensive (and well documented) library to interactive with lots of the Amazon services

jsonfield:
    the most comprehensive (and bug free) implementation of a model field that stores json.

django-bitfield:
    a model field where you can set / clear individual bits in a sequences.

celery:
    asynchronous task management.

django-haystack:
    inteface to the apache solr (lucene) search engine, providing a QuerySet-like interface.

django-sekizai:
    css / jss file management, creating a cached file combining all css or js into a single file to help download performance

django-compressor:
    css / js file compression utility which can be used in conjunction with sekizai to pre-process or compress. see :ref:`static-file-management`

django-fsm:
    facilities for creating a finite-state machine for a model

django-retracer:
    simple utility that helps you store / retrieve origin pages

django-tastypie:
    "instant" ReST interface, created automagically based on django models
    
django-bootstrap-form:
    template tag filter for displayng a django form with the right classes & structure for bootstrap 3
    
django-admin-bootstrapped:
    skin / theme for django admin using bootstrap so it looks modern


Install Flags
-------------------------

WITH_GEVENT:
    multi-threading capabilities for python. requires uwsgi, which is also installed with this flag
    
WITH_MYSQL:
    postgres is the default. this installs mysql support for python instead
    
SERVER_INSTALL:
    installs uwsgi for running in a production environment. uwsgi can also be used for development purposes (see :ref:`wsgi-application`)



Package Recommendations
---------------------------

While I use these packages less frequently, these are better than other varients.

python-social:
    replacement for django-social-auth. documentation isn't great, but it easily integrates with 
    
lxml:
    <description> including STATIC_DEPS
    
beautifulsoup, beautifulsoup4:
    required by compressor
    
