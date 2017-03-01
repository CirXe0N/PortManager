from django.shortcuts import render, get_object_or_404
from web.models import Dock, CargoHazard


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
