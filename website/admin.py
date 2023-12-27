from django.contrib import admin
from .models import *

admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(PollingUnit)
admin.site.register(Party)
admin.site.register(AnnouncedPuResult)