from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Legal(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    document_type = models.CharField(max_length=500)
    document_title = models.CharField(max_length=500)
    security_level =models.CharField(max_length=500)
    investigation_number = models.CharField(max_length=500)
    investigation_phase =models.CharField(max_length=500)
    investigation_status =models.CharField(max_length=500)
    investigation_title = models.CharField(max_length=500)
    investigation_type = models.CharField(max_length=500)
    firm_organization = models.CharField(max_length=500)
    filedby = models.CharField(max_length=500)
    onbehalfof = models.CharField(max_length=500)
    documentdate = models.DateTimeField('Document Date')
    officialrecieveddate= models.DateTimeField('Received Date')
    document_link = models.CharField(max_length=500)
    modified_date = models.DateTimeField('Modified Date')    

   
