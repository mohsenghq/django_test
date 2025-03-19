from django.shortcuts import render, redirect
from .forms import ContactUsForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model

def home_page(request):
    context = {
        'title': 'Home',
        'message': 'This is home page'
    }
    return render(request, 'home.html', context)


def contact_us_page(request):
    contact_us_form = ContactUsForm()
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('email'))
        print(request.POST.get('message'))
    context = {
        'title': 'Contact Us',
        'message': 'This is contact us page',
        'contact_us_form': contact_us_form
    }
    return render(request, 'contact-us.html', context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        # print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error: Invalid username or password')
    context = {
        'title': 'Login',
        'message': 'This is login page',
        'login_form': login_form
    }
    return render(request, 'auth/login.html', context)

User = get_user_model()

def register_page(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=username, email=email, password=password)
    context = {
        'title': 'Register',
        'message': 'This is register page',
        'register_form': register_form
    }
    return render(request, 'auth/register.html', context)