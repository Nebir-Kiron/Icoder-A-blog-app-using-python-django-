from django.db import models

# Create your models here.
class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=13)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True,blank=True)