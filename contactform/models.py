from django.db import models
from django.utils import timezone
from django.conf import settings

class contact_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    enquiry = models.TextField()
    enquiry_date = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return "Name: " + self.name + " - Email: " + self.email
