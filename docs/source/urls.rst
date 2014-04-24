url patterns
======================================


there are cases when certain views take optional parameters. often times these are
provided within the ``url`` generator funtion. for example, when using django's
authentication login view:

    def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

the ``url`` generator function looks like this:

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name':'registration/login.html',
            'authentication_form':EmailAuthenticationForm
        },
        name="login"),
        
however, it is possible also to provide optional parameters within
the url pattern itself using this format:

    ``(?:/(?P<sport>[a-z\s]*))?``

explaination: the outer grouping `()?` is the regex pattern for optional. however,
the ``?:`` is necessary to capture the sub-expression enclosed by the commonly used
``(?P<name>)`` expression.





These two patterns can combined:

    url(r'^t/(?P<slug>[A-Za-z][a-zA-Z0-9\-]+?)/$, OrganizationView.as_view(), name="organization"),
    url(r'^t/(?P<slug>[A-Za-z][a-zA-Z0-9\-]+?)/(?P<sport>[a-z\s]*)/$', OrganizationView.as_view(), name="organization-with-sports"),

into:

    url(r'^t/(?P<slug>[A-Za-z][a-zA-Z0-9\-]+?)(?:/(?P<sport>[a-z\s]*))?/connects(?:/(?P<year>[0-9]{4}))?/?$', OrganizationView.as_view(), name="organization"),

which elimintes duplicate code (DRY) and tracking two different url name resolutions:

    from django.core.urlresolvers import 





url(r'^t/(?P<slug>[A-Za-z][a-zA-Z0-9\-]+?)(?:/(?P<sport>[a-z\s]*))?/connects(?:/(?P<year>[0-9]{4}))?/?$', OrganizationView.as_view(), {'root':'connects'}, name="connections-team"),