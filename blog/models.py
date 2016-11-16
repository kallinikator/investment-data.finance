from django.db import models

class Entry(models.Model):
    """ Contains all information about a blogentry """
    date = models.DateField()
    title = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        ordering = ['date']
        
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title