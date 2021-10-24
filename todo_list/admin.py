from django.contrib import admin
from .models import List #.models indicates the current file folder (naka tudlo sya sa models.py)
from .models import Contact
from .models import profile
admin.site.register(List)
admin.site.register(Contact)
admin.site.register(profile)

# Register your models here.
