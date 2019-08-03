from django.db import models

# Becareful when working here. any mishap can fry the entire system for people
class Party(models.Model):
    id = models.AutoField( primary_key=True )
    start = models.TimeField( auto_now=False, auto_now_add=False )
    end = models.TimeField( auto_now=False, auto_now_add=False )
    date = models.DateField( auto_now=False, auto_now_add=False ) # date happening
    address = models.TextField()
    rate = models.TextField()
    status = models.CharField( max_length=200 )
    track_time = models.TimeField( auto_now_add=True )

