from django.contrib.auth.models import Group
from django.contrib import admin
from .models import User, UserProfile, Hobby
# Register your models here.

# unregister group
admin.site.unregister(Group)

class Useradmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username' )


admin.site.register(User, Useradmin)
admin.site.register(UserProfile)
admin.site.register(Hobby)

