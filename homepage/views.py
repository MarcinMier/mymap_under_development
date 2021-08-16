from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users.views import register
from homepage.models import Route


# jeżeli użytkownik jest niezalogowany przekierowujemy na stronę logowania
@login_required()
def home(request):

    # wyciągamy usera
    user = request.user

    # Z bazy wyciągamy wszystkie trasy przypisane do danego użytkownika
    routes = Route.objects.filter(user=user)

    return render(
        request,
        'homepage/routes.html',
        context={
            'routes': routes  # trasy przekazujemy w kontekście do szablony (a w szablonie iterujemy się po nich)
        }
    )

    # if request.user.is_authenticated:
    #     return redirect('/users/profile.html') # nie mam pojecia jak zrobic to inaczej
    # else:
    #     return register(request)


@login_required
def about(request):
    return render(request, 'homepage/about.html')