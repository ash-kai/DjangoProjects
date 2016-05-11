from django.contrib import admin

# Register your models here.
from .models import Account, Notification, Task
admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Task)
