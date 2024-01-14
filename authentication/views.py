from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')



    return render(request, "authentication/signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        try:
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            
            myuser.first_name = fname
            myuser.last_name = lname

            myuser.save()

            messages.success(request, "Your account has been signed up")
            return redirect('signin')
        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect('signup')

    return render(request, "authentication/signup.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!!")
    return redirect('home')