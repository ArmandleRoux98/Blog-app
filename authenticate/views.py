from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    """
    GET - Returns page with form to register a new user.
    POST - Attempts to create new user, logs them in and redirect to 
           home on success or redirect back to register page.
    """
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
    """Clears user's session and logs them out."""
    logout(request)
    return redirect('blog_app:home')