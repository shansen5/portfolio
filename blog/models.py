from django.db import models

class Blog( models.Model ):
    image = models.ImageField( upload_to='images/' )
    body = models.TextField( max_length=2000 )
    title = models.CharField( max_length=255 )
    pub_date = models.DateTimeField()
    body = models.TextField()

