from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

# Create your models here.
class Player(models.Model):
    name = models.CharField("ニックネーム",max_length=20)
    #なんか出てくるから保留
    # sns = models.URLField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


class Job(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)
    explain = models.CharField(max_length=20)
    skillpoint = models.IntegerField(default=0)
    last_used = models.DateTimeField(default=timezone.now)
    main = models.IntegerField(default=1)
    player_num = models.ForeignKey(Player,on_delete=models.CASCADE)
    token = models.UUIDField(unique=True,default=uuid.uuid1())

class Skill(models.Model):
    name = models.CharField(max_length=10)
    level = models.IntegerField(default=1)
    explain = models.CharField(max_length=20)
    Job_num = models.ForeignKey(Job,on_delete=models.CASCADE)
    token = models.UUIDField(unique=True,default=uuid.uuid1())

class Task(models.Model):
    what = models.CharField(max_length=30)
    time = models.IntegerField(default=0)
    when = models.DateTimeField(default=timezone.now)
    player_num = models.ForeignKey(Player,on_delete=models.CASCADE)
    Job_num = models.ForeignKey(Job,on_delete=models.CASCADE)
    token = models.UUIDField(unique=True,default=uuid.uuid1())