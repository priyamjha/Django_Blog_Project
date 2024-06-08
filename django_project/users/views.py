from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm


# register user
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Thankyou for registering. Please kindly login')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register')
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


# login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request,'Something went wrong')
    else:
        return render(request, 'users/login.html')


# logout user
def logout_user(request):
    logout(request)
    messages.info(request,'Sessions has ended. LOGIN Again')
    return redirect('login')