mirskutils.contentblocks
======================================

There are numerous django-based content management systems[1]_[2]_ available, providing
full-fledged applications that stack up well against others in the industry drupal,
wordpress, etc. However, often times a developer only needs to a developer only needs
to enable an administrator to edit sections or snippets of content that are embedded
throughout the web application. In this case, the existing CMSs are cumbersome and
often assume that the application is based around them and not as a component to another
web application.

ContentBlocks are intended to be a simple way of providing "static" editing capabilities
to a user without giving the capability of mucking with the site's style and layout.

- one or more paragraphs of text (limited styles to bold, italic, underline, lists)

- playlist of videos 

- a series of images

- a collection, in a ranked order, of other contentblocks


.. [1] https://www.djangopackages.com/grids/g/cms/
.. [2] https://code.djangoproject.com/wiki/CMSAppsComparison

Content Block Model
--------------------------------------

.. automodule:: mirskutils.content.models
   :members: ContentBlock
   
Template Tags
---------------------------------------   

.. automodule:: contentblock_exists, contentblock_as_divs, contentblock



