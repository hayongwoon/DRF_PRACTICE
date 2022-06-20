from django.contrib import admin
from product.models import Event as EventModel
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'register_date', 'thumbnail')

admin.site.register(EventModel, EventAdmin)

