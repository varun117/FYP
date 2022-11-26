from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_info =  models.ForeignKey(userinfo,on_delete=models.CASCADE)
    gender = models.CharField(max_length = 10 , default="Male")
    address = models.CharField(max_length=200, blank = True)
    phone = models.CharField(max_length=200, blank = True)
    birthday = models.DateField(default = timezone.now)
    visit = models.BooleanField(max_length=3)
    date = models.DateField(default = timezone.now)
    time = models.CharField(max_length=200, blank = True, null = True)
    reason = models.CharField(max_length=200, blank = True, null = True)
    scanned_pic = models.ImageField(upload_to='scanned_pic/')

    def __str__(self):
        return self.user.first_name
