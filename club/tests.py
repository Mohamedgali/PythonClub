from django.test import TestCase
from .models import Meetings, MeetingMinutes, Resource, Event

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