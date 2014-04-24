mirskutils.views
======================================

Class-based views are an improved way of organizing view functions, including being
able to inherit functionality from super-class (or mixins). As they are new as of
django 1.4, not all packages have been convereted over to using them.

background
--------------------------------------


django url router calls `dispatch` method, which, by default, determines the kind of
request and calls the appropriate method to handle the request:
     
* GET request -> `def get(self, request, ...)`
* POST request -> `def post(self, request, ...)`
* DELETE request -> `def delete(self, request, ...)`
* etc
     
if the class method associated with the request does not exist, an HttpMethodNotAllowed (405) is returned

the django.views.generic.View base-class has a static-method `as_view()` which provides an instance of the
view class for the django router to reference / call::

    url(r'^home/', Home.as_view(), name="home")

migration
--------------------------------------

the intention is to break get and post handlers into separate functions so that
the originally recommended django GET/POST pattern::

    def handle_information_form(request):
        form = InformationForm()
        
        if request.POST:
            form = InformationForm(request.POST)
            if form.is_valid():
                ...
                ...
                return render(request, 'template.html', {})
        return render(request, 'template.html', {'form':form})

becomes this::

    from django.views.generic import View


    class HandleInfo(View):
        def get(self, request):
            return render(request, 'template.html', {'form':InformationForm()})
            
        def post(self, request):
            form = InformationForm(request.POST)
            if form.is_valid():
                ...
                ...
                return render(request, 'template.html', {})
            return render(request, 'template.html', {'form':form})                

migration-lite
--------------------------------------

migrations can be expensive, increase risk and break already working things. instead,
the move towards class-based views can be done in a phased approach, by using the
`dispatch` method as an equivalent to your original function. this is *not* best-practice::


    class HandleInfo(View):
    
        def dispatch(self, request):
        
            form = InformationForm()
        
            if request.POST:
                form = InformationForm(request.POST)
                if form.is_valid():
                    ...
                    ...
                    return render(request, 'template.html', {})
            return render(request, 'template.html', {'form':form})



authenticated views
--------------------------------------


.. automodule:: mirskutils.views
    :members: