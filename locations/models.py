from django.db import models

class mapDetails(models.Model):
    center1 = models.CharField(max_length=10)
    center2 = models.CharField(max_length=10)
    name = models.CharField(null=True, max_length=250)
    zoom = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)

    def __unicode__(self):
        return self.name
    #51.5041458,0.0030516,