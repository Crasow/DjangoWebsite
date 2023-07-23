from django.http import HttpResponse
from django.views.generic import View

class HelloWorldView(View):
    def get(self, *args):
        return HttpResponse("Hello world!")

def check_kwargs(request, **kwargs):    
    return HttpResponse(f"kwargs:<br>{list(kwargs.keys())[0]} --- {kwargs['word']}")