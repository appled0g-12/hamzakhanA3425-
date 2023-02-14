from audioop import reverse
from django.db import models
from django.contrib.auth.models import User

class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card')
    image = models.ImageField(upload_to='pro/', null=True)
    name = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    perfect_in = models.CharField(max_length=255, null=True)
    years_of_experience  = models.CharField(max_length=255, null=True)
    availability  = models.CharField(max_length=255, null=True)
    pricing = models.CharField(max_length=255, null=True)
    trained_at = models.CharField(max_length=255, null=True)
    additional_text = models.CharField(max_length=500, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    likes = models.ManyToManyField(User,related_name='like',blank=True)

    def __str__(self):
        return self.name
    

class WorkDoneImages(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='workdone')
    workimage = models.ImageField(upload_to='workdonepic/',blank=True,null=True)
    

