from django.contrib import admin
from .models import Activity, ActivityMaster, ActivityChild


admin.site.register(Activity)
admin.site.register(ActivityMaster)
admin.site.register(ActivityChild)
