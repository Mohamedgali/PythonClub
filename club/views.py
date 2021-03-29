from django.shortcuts import render, get_object_or_404
from .models import Meetings, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'club/index.html')

@login_required
def meetings(request):
    meeting_list=Meetings.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})
@login_required
def meetingDetail(request, id):
    meeting=get_object_or_404(Meetings, pk=id)
    return render(request, 'club/meeting_detail.html', {'meeting' : meeting})
@login_required
def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})
@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html',{'form': form})
@login_required
def newResource(request):
    form = ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html',{'form':form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')     