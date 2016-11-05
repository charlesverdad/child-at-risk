from django.contrib import admin

from .models import Child, Staff, Relative, Home

# Register your models here.
admin.site.register(Child)
admin.site.register(Staff)
admin.site.register(Relative)
admin.site.register(Home)
