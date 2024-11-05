from django.db import models

from django.db import models

class CallRecord(models.Model):
    CALL_TYPE_CHOICES = (
        ('start', 'Start'),
        ('end', 'End'),
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=5, choices=CALL_TYPE_CHOICES)
    timestamp = models.DateTimeField()
    call_id = models.CharField(max_length=20, unique=True)
    source = models.CharField(max_length=11, blank=True, null=True) 
    destination = models.CharField(max_length=11, blank=True, null=True)  
