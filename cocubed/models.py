from django.db import models

class Attendee( models.Model ):
    image_url = models.CharField( max_length=80 )
    role = models.CharField( max_length=40 )
    first_name = models.CharField( max_length=40 )
    last_name = models.CharField( max_length=40 )
    email = models.CharField( max_length=60 )
    username = models.CharField( max_length=20 )
    password = models.CharField( max_length=20 )
    summary = models.TextField( max_length=2000 )
