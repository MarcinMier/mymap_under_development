from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.views import register


def home(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html') # nie mam pojecia jak zrobic to inaczej
    else:
        return register(request)


@login_required
def about(request):
    return render(request, 'homepage/about.html')