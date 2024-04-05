from django.shortcuts import get_object_or_404, render
from django.utils.timezone import localtime
from datacenter.models import Passcard, Visit
from datetime import timedelta


def is_strange_visit(visit):
    entered_at = localtime(visit.entered_at)
    leaved_at = localtime(visit.leaved_at) if visit.leaved_at else localtime()
    duration = leaved_at - entered_at
    return duration > timedelta(hours=1)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    
    visits_info = [{
        'entered_at': localtime(visit.entered_at),
        'leaved_at': localtime(visit.leaved_at) if visit.leaved_at else None,
        'duration': (localtime(visit.leaved_at) - localtime(visit.entered_at)) if visit.leaved_at else None,
        'is_strange': is_strange_visit(visit)
    } for visit in passcard_visits]
    
    context = {
        'passcard': passcard,
        'visits_info': visits_info
    }
    return render(request, 'passcard_info.html', context)
