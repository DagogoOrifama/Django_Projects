from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# custom view for the registration form
def register(request):
    # check if form is submitted
    if request.method == 'POST':
        # get the submited form
        form = RegisterForm(request.POST)
        # check if the form data is valid
        if form.is_valid():
            # save the user
            form.save()
            # get the username inputted during registeration
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

# def register(request):
#     # check if form is submitted
#     if request.method == 'POST':
#         # get the submited form
#         form = UserCreationForm(request.POST)
#         # check if the form data is valid
#         if form.is_valid():
#             # save the user
#             form.save()
#             # get the username inputted during registeration
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Welcome {username}, your account is created')
#             return redirect('food:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form':form})

@login_required #restricts users who are not logged in to access the view
# create view for profile page
def profilepage(request):
    return render(request, 'users/profile.html')