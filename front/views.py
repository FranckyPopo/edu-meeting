from django.shortcuts import render
from django.http import HttpResponse
from features.models import ContactUs


def front_index(request):
    return render(request, "front/pages/index.html")


def front_meeting_details(request):
    return render(request, "front/pages/meeting-details.html")


def front_meetings(request):
    return render(request, "front/pages/meetings.html")