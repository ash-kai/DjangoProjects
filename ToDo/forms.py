from django import forms
from django.contrib.auth.models import User
from .models import Account, Notification, Task, UserProfile

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
    # i can set datetime field, when i would include it back to have auto date property set to true.       
    class Meta:
	model = Task		
	fields = ['task_title','task_description','creator','notify']
        exclude = ['created_date']

    def clean(self):
	pass
	#Add logic here to set the date value proper
	#use cleaned_data dictionary

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
	model = User
	fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
	model = UserProfile
	fields = ['phone_number']
