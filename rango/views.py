from django.shortcuts import render
from allauth.account.views import SignupView
from allauth.account.forms import LoginForm
from django.http import HttpResponse
from models import *
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'demo/index.html', context_dict)
    #return HttpResponse("Rango says hey there world! <br/> <a href='/demo/about'>About</a>")

def about(request):
    context_dict = {'boldmessage': "This is about page"}
    return render(request, 'demo/about.html', context_dict)

class CustomSignupView(SignupView):
    # here we add some context to the already existing context
    def get_context_data(self, **kwargs):
        # we get context data from original view
        context = super(CustomSignupView,
                        self).get_context_data(self, **kwargs)
        context['login_form'] = LoginForm() # add form to context
        return context

from allauth.account.signals import user_signed_up
from django.dispatch import receiver