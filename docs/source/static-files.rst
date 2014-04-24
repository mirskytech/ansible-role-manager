.. _static-file-management:

static file management
==============================================

environment configuration
-------------------------------------

By convention, the django project template included in this package uses::

    STATIC_ROOT = os.path.join(PROJECT_PATH, "site_static")
    STATIC_URL = "/static/"

During development (ie `DEBUG=True`), the django.static.staticfiles handler
will find all your various static files. In production, run ``./manage.py collectatic``
to gather all the static files.


import statements
-------------------------------------

This setup will also allow you to have import statements, but the paths need to be relative to `static`.

for example, if your static file is in ``myapp/static/myapp/mylessfile.less``, the import statement would be::

    @import "/static/script/textarea.css";


css (and less,sass) and javascript
----------------------------------------------

The project template is setup with sekizai tags (a convenient way of 
specifiy your scripts in any page but all of them rendering in one place) and 
compress (preprocessor of files as well as concatenation & minimization). To enable 
the precompilers, uncomment this line towards the bottom of the `settings.py` file::


    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )
    
    
included static file libraries
-----------------------------------------------

* bootstrap (version 2)

twitter's cross platform & device library
http://getbootstrap.com/2.3.2/

* bootstrap3

twitter's cross platform & device library
http://getbootstrap.com/

* canjs

javascript mvc framework, forked (formerly known as?) sproutcore
works with jQuery, Zepto, Dojo, Mootools, YUI
http://canjs.com

* emberjs
* glyphicons
* html5shiv
* jquery
    * anythingslider.css
    * imagesloaded.min.js
    * jquery.ajaxform.js
    * jquery.anythingslider.min.js
    * jquery.cookie.js
    * jquery.infieldlabel.js
    * jquery.placeholder.js
    * jquery.qtip.css
    * jquery.qtip.js
    * jquery.selectboxit.js
    * jquery.tooltipster.js
    * jquery.tooltipster.min.js
    * selectboxit.css
    * themes
    * tooltipster.css
* jqueryui
* reset.css
* respondjs
* select2
* selectize
* tinymce
* wijmo