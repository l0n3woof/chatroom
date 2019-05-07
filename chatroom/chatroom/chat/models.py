from django.db import models

# Create your models here.

class history(models.Model):
    main_id = models.AutoField(primary_key=True)
    u_id = models.CharField(max_length=30, null=True, default=0)
    messages = models.TextField()
    cnl = models.CharField(max_length=30, null=True, default=0)
