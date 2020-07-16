from django.db import models

# Create your models here.
class Post(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=25)
    slug = models.CharField(max_length=120)
    content = models.TextField()
    time = models.DateTimeField(blank=True)
    

    def __str__(self):
        return f'{self.title} by {self.author}'