from django.contrib import admin

# Register your models here.

from .models import Relationship,Person

admin.site.register(Relationship)
admin.site.register(Person)
