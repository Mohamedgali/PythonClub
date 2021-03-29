from django.test import TestCase
from .models import Meetings, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse


# Create your tests here.
class MeetingsTest(TestCase):
    def setUp(self):
        self.type=Meetings(meetingtitle='Conference')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Conference')


    def test_tablename(self): 
        self.assertEqual(str(Meetings._meta.db_table), 'meeting') 

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(minutestext='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(Event._meta.db_table), 'event')

class newMeetingForm(TestCase):
    def test_meetingform(self):
        data={
            'meetingtitle':'New Project',
            'meetingdate':'March 20, 2021',
            'meetingtime':'9:00',
            'location':'Seattle',
            'agenda':'Developing new project.',
            
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class newResourceForm(TestCase):
    def test_resourceform(self):  
        data={
            'resourcename':'shop',
            'resourcetype':'stuff',
            'URL':'https:www.moe',
            'dateentered':'3-20-2021',
            'userid':'mohamed',
            'description':'shopping stuff ',
        }
        form=ResourceForm (data) 
        self.assertTrue(form.is_valid)



class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinutes.objects.create(meetingname = 'Meeting Class')
        self.meeting = Meetings.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeetings'))    
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeetings/')


class New_MeetingMinute_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinutes.objects.create(meetingname = 'Meeting Class')
        self.meeting = Meetings.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))
        self.meetingminute = MeetingMinutes.objects.create(minutesdescription = 'Have fun!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeetingminutes'))    
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/newmeetingminutes/')


class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password =  'P@ssw0rd!')
        self.type = MeetingMinutes.objects.create(meetingname = 'Meeting Class')
        self.meetingminute = MeetingMinutes.objects.create(minutesdescription = 'Have fun!')
        self.meeting = Meetings.objects.create(meetingtitle = 'Django Super Fun Class', meetingtype = self.type, user = self.test_user, dateentered = datetime.date(2021,1,29), meetinglocation = 'Seattle', meetingtime = datetime.time(22,55,29))
        self.resource = Resource.objects.create(name = 'Django Super Class', location = 'Seattle', user = self.test_user, meeting = self.meeting, date = datetime.date(2021,1,29), time = datetime.time(22,55,29), text = 'Have Fun!', url='http://www.meeting.com', description="Meeting is so much fun!")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresources'))    
        self.assertRedirects(response, '/accounts/login/?next=/club/newresources/')