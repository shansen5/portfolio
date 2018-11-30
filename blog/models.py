from django.db import models

class Blog( models.Model ):
    image = models.ImageField( upload_to='images/' )
    body = models.TextField( max_length=2000 )
    title = models.CharField( max_length=255 )
    pub_date = models.DateTimeField()

    def __str__( self ):
        return self.title

    def summary( self ):
        summary = self.body[:200]
        if ( len( self.body ) > 200 ):
            summary += "..."
        return summary
    
    def pub_date_pretty( self ):
        return self.pub_date.strftime( '%b %e %Y' )