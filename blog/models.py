from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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

class BlogComment(models.Model):
    si_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.comment[0:13]}.... : by {self.user.username}'    