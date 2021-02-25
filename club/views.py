from django.shortcuts import render, get_object_or_404
from .models import Meetings, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meetings(request):
    meeting_list=Meetings.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meetings, pk=id)
    return render(request, 'club/meeting_detail.html', {'meeting' : meeting})

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})

