from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('community:index')


def profile(request, username):
    # class 유저 전체다 가져옴
    User = get_user_model()
    # instance username이 일치하는 경우
    profile_user = get_object_or_404(User, username=username)
    context = {
        'profile_user' : profile_user,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, pk):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=pk)
    if me in you.followers.all():
        me.followings.remove(you)
    else:
        me.followings.add(you)
    return redirect('accounts:profile', you.username)


# follow() got an unexpected keyword argument 'username'
# typeerror - pk가 와야하는데 username들어옴
# 'User' object has no attribute 'followers'