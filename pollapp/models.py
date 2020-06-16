from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact_no=PhoneNumberField()
    subject=models.CharField(max_length=100)
    issue=models.TextField(max_length=1000)
    time=models.DateTimeField(auto_now_add=True)
    solved=models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    class Meta:
        ordering = ('-time',)
class Polls(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    decription=models.TextField(max_length=500,blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200,blank=True,default="None")
    option4=models.CharField(max_length=200,blank=True,default="None")
    option5=models.CharField(max_length=200,blank=True,default="None")
    option6=models.CharField(max_length=200,blank=True,default="None")
    option7=models.CharField(max_length=200,blank=True,default="None")
    option8=models.CharField(max_length=200,blank=True,default="None")
    
    option1_count=models.IntegerField(default=0)
    option2_count=models.IntegerField(default=0)
    option3_count=models.IntegerField(default=0)
    option4_count=models.IntegerField(default=0)
    option5_count=models.IntegerField(default=0)
    option6_count=models.IntegerField(default=0)
    option7_count=models.IntegerField(default=0)
    option8_count=models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-create_time',)    

