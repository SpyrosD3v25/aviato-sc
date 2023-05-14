from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import CreateView
from .models import Person
from django.views.generic import UpdateView
from home.models import Person
from home.forms import PersonForm, MessageForm
from django.contrib import messages


def assistant(request, *args, **kwargs):
    if request.user.is_authenticated == False:
        return login(request)

    return render(request, "home/assistant.html", {"form" : MessageForm})

def login(request):
    # PersonForm = PersonForm(request)
    return render(request, "home/LoginPage.html", {"form" : PersonForm})


def register(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            print("sdfa")
            user = form.save()

            user_instance = Person.objects.create(username=user.username)


            messages.success(request, "Registration successful." )
            redirect("home:assistant")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = PersonForm()
    return render (request=request, template_name="home/SignUpPage.html", context={"form":form})