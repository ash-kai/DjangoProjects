from django.contrib import admin

# Register your models here.
from .models import Account, Notification, Task, UserProfile

class AccountAdmin(admin.ModelAdmin):
    list_display = ("__unicode__","first_name","last_name")
    list_filter = ("first_name", "last_name")
    class Meta:
	model = Account


admin.site.register(Account,AccountAdmin)
admin.site.register(Notification)
admin.site.register(Task)
admin.site.register(UserProfile)

