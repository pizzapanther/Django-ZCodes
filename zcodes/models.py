from django.contrib.gis.db import models

class ZipCode (models.Model):
  code = models.CharField("Zip Code", max_length=20)
  country = models.CharField(max_length=2)
  city = models.CharField(max_length=200, blank=True, null=True)
  state = models.CharField(max_length=2, blank=True, null=True)
  timezone = models.CharField(max_length=25, blank=True, null=True)
  location = models.PointField(null=True, blank=True)
  
  class Meta:
    unique_together = ('code', 'country')
    
  def __unicode__ (self):
    return self.code
    
  def __str__ (self):
    return self.code
    
  @staticmethod
  def autocomplete_search_fields():
    return ("id__iexact", "code__icontains", "city", "state", "timezone", "country")
    
