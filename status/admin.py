from django.contrib import admin
from status.models import Status

# Register your models here.

#For showing the Status in the Admin panel
class StatusAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'user', 'image_link')
    
admin.site.register(Status, StatusAdmin)
