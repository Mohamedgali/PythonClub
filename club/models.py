from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meetings(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()    
    meetingtime=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    agenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitle 
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meetings, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)   
    minutestext=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.minutestext
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    URL=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource' 

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.CharField(max_length=255)
    description=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'