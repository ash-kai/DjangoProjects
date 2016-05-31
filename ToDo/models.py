from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from djago.core.urlresolvers import reverse


# Create your models here.

#Class structure for User-Account
class Account(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 15)
    email_id = models.EmailField(unique=True)

    def __unicode__(self):
	return ' '.join([self.first_name,self.last_name])


#Class structure for Notification
class Notification(models.Model):
    notification_type = models.CharField(max_length=20,default=None)
    
    def __str__(self):
	return self.notification_type


#Class structure for Task
class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500)
    due_date = models.DateTimeField('Due Date', blank=True)
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    notify = models.ForeignKey(Notification, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.task_title

    def get_absolute_url(self):
        return reverse("", kwargs={"slug":self.slug})


#Going to replace Account class
#Represents the profile of the Users for the app
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_number = models.CharField(max_length=15)

    def __unicode__(self):
	return self.user.username
