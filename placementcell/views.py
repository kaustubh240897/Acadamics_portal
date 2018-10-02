from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import Recruiter_register_form,LoginForm


def home_page(request):
    context = {"content": "Welcome to home page"}

    return render(request, 'home_page.html', context)


class Recruiter_registerView(View):
    form_class = Recruiter_register_form
    template_name = 'Recruiter_registration.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process from data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            #clean and normalize data
            username = form.cleaned_data['username']
            organisation_name=form.cleaned_data['organisation_name']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']

            user.set_password(password)

            user.save()

            # returns user objects if credentials are correct
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return redirect("/")

        return render(request, self.template_name, {'form': form})


def login_page(request, username=None):
    form= LoginForm(request.POST or None)

    context = {
        "form": form
    }
    print("user logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            # context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
            # Return an 'invalid login' error message.


    return render(request, "login.html", context)


