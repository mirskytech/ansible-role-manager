

project template
======================================

a quick way of creating a new project with the most common elements already existing::

    project/
        manage.py  # django project management
        wsgi.py    # web application entry point
        conf/      # sample configuration files for the project
        docs/      # initial sphinx documentation setup
        mobileapp/ # location (currently empty) for the project's mobile app
        webapp/    # django project struction
        
        



web application
----------------------------------------

The django portion -- under `webapp/` -- includes this structure and elements::

    webapp/
        api.py                      # location for any api instantiations
        basic_init.sample.json      # example of a fixture
        core/                       # core applications of this project
            fhfh
        registration/               # urls, configuration and templates for django.contrib.auth
        routers.py                  # 
        settings.py
        static
        templates
        urls.py
        wingstub.py
        
api.py:
    location for any api singleton instantiations

basic_init.sample.json:
    example of a django fixture for loading data
    
core:
    location for the core applications of this project
    
routers.py:
    a utility to direct all models of a certain type to a specified database
    
settings.py:
    basic configuration
    
static:
    project-wide static files
    
templates:
    base, 404, 500 and 403 templates
    
urls.py:
    master url file with examples
    
wingstub.py:
    utility to connect to WingIDE's remote debugging