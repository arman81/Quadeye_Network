from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

DC_TYPE = (
    ('source','source'),
    ('dest','dest'),
	)

LINK_TYPE = (
    ('Upcoming','Upcoming'),
    ('Est','Est'),
	)
class dataCentre(models.Model):
    name = models.CharField(max_length=10,unique=True)
    region = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10 , null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, null=True)

    def __str__(self):
        return self.name


class link(models.Model):
    linkname = models.CharField(max_length=30)
    linktype = models.CharField(max_length=1,choices=LINK_TYPE,default='NA')
    ass_dc = models.ForeignKey(dataCentre,default=None)
    latency = models.DecimalField(max_digits=20, decimal_places=10,null=True)
    dc_type = models.CharField(max_length=1,choices=DC_TYPE,default='NA')
    
    def __str__(self):
        return self.linkname	