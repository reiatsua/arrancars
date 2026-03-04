
from django.shortcuts import render
from .models import TeamMember, Match, TeamInfo

def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html', {
        'players': TeamMember.objects.all()
    })

def matches(request):
    return render(request, 'matches.html', {
        'matches': Match.objects.all()
    })

def about(request):
    team = TeamInfo.objects.first()
    return render(request, "about.html", {
        "team": team
    })