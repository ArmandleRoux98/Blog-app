from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_user(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "authenticate/registration.html", context={'form':form})
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            else:
                return(redirect('authenticate:register'))
        else:
            return render(request, "authenticate/registration.html", context={'form':form})
        return redirect('blog_app:home')
    
def sign_user_out(request):
    logout(request)
    return redirect('blog_app:home')