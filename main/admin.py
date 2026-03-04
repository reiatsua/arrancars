from django.contrib import admin
from .models import TeamInfo, TeamMember, Match


@admin.register(TeamInfo)
class TeamInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "discipline", "goal")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("nickname", "role")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("opponent", "result", "date")