from django.db import models
from django.conf import settings
from django.utils import timezone

class Magazine(models.Model):

    name = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.name

class Purchase(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    magazine = models.ForeignKey(Magazine)
    subscription_end = models.DateTimeField(default=timezone.now)

    #def __unicode__(self):
        #return self.user + " " + self.magazine