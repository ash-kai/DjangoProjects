from django import forms
from .models import Account, Notification, Task

#ModelForm for User-Account class
class AccountForm(forms.ModelForm):
    class Meta:
	model = Account
	fields = "__all__"

#ModelForm for Notification class
class NotificationForm(forms.ModelForm):
    class Meta:
	model = Notification
	fields = "__all__"

#ModelForm for Task class
class TaskForm(forms.ModelForm):        
    class Meta:
	model = Task		
	fields = ['task_title','task_description','creator','notify']
        exclude = ['created_date']

