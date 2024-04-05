from django.utils.timezone import localtime
from datetime import datetime, timedelta
from datacenter.models import Visit
from django.shortcuts import render


def is_strange_visit(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    duration = leaved_at - entered_at
    return duration > timedelta(hours=1)


def storage_information_view(request):
    unleft_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in unleft_visits:
        who_entered = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at).replace(microsecond=0)
        duration = localtime() - entered_at
        is_strange = is_strange_visit(visit)
        non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_strange
        })
    
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
