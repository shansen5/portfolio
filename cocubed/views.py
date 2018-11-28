from django.shortcuts import render
from .models import Attendee

def attendees( request ):
    attendees = Attendee.objects
    return render( request, 'cocubed/attendees.html', {'attendees':attendees} ) 