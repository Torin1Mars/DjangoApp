from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def register_view(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("posts:post_list")
    else:
        #Empty form
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("posts:post_list")
    else:
        form = AuthenticationForm()
    return render(request, 'users/loging.html', {'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")  #Redirect to home
