from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 15)
    email_id = models.EmailField(unique=True)

    def __str__(self):
	return ' '.join([self.first_name,self.last_name])


class Notification(models.Model):
    notification_type = models.CharField(max_length=20,default=None)
    
    def __str__(self):
	return self.notification_type
	


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500)
    due_date = models.DateTimeField('Due Date')
    creator = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.now)
    notify = models.ForeignKey(Notification, on_delete=models.CASCADE)

    def __str__(self):
	return self.task_title

