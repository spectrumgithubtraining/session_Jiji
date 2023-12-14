# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()

        if user:
            # User is authenticated, set session variable
            request.session['username'] = user.username  # Use username in the session
            messages.success(request, 'Login successful.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def dashboard(request):
    username = request.session.get('username')
    if username:
        return render(request, 'dashboard.html', {'username': username})
    else:
        messages.error(request, 'You are not logged in.')
        return redirect('login')

def logout(request):
    # Clear session data
    request.session.clear()
    messages.success(request, 'Logout successful.')
    return redirect('login')
