from django.contrib import admin
from django import forms
from django.contrib.gis.db import models

from zcodes.models import ZipCode

class ZipCodeAdmin (admin.ModelAdmin):
  list_display = ('code', 'city', 'state', 'country', 'timezone')
  search_fields = ('code', 'city', 'state')
  list_filter = ('country', 'state', 'timezone')
  
  formfield_overrides = {
    models.PointField: {'widget': forms.TextInput},
  }
  
admin.site.register(ZipCode, ZipCodeAdmin)
