from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.authtoken.models import Token

from web.models import Dock, CargoHazard, DockSupervisor, Person, Ship


def dock_overview(request):
    template = 'web/dock/dock_overview.html'
    context = {
        'data': []
    }

    docks = Dock.objects.all()
    for dock in docks:
        hazards = CargoHazard.objects.filter(container__ship__dock=dock).distinct()
        context['data'].append({
            'dock': dock,
            'hazards': hazards
        })

    return render(request, template, context)


def dock_details(request, dock_id):
    template = 'web/dock/dock_details.html'

    context = {
        'dock': get_object_or_404(Dock, dock_id=dock_id)
    }

    return render(request, template, context)


def authentication(request):
    template = 'web/authentication/authentication.html'

    context = {
        'is_failed_login': False,
    }

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        supervisor = DockSupervisor.objects.filter(employee__person__user=user)

        if len(supervisor) > 0:
            login(request, user)
            return redirect('dock_overview')
        else:
            context['is_failed_login'] = True

    return render(request, template, context)


def do_logout_request(request):
    logout(request)
    return redirect('dock_overview')


def user_profile(request):
    template = 'web/profile/user_profile.html'
    person = get_object_or_404(Person, user=request.user)
    ships = Ship.objects.filter(captain__person=person)
    token = Token.objects.filter(user=request.user).first()

    context = {
        'person': person,
        'ships': ships,
        'token': token,
    }

    return render(request, template, context)
