from django import forms
from .models import Account

class NameForm(forms.Form):
    your_name = forms.CharField(label='YName', max_length=50)


class AccountForm(forms.ModelForm):
    class Meta:
	model = Account
	fields = "__all__"
