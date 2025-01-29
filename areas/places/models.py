from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_photo = models.ImageField(upload_to='media/',blank=True)
    is_premium = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Account of {self.user}'

BHK_CHOICE = (
    ('1','1BHK'),
    ('2','2BHK'),
    ('3','3BHK'),
    ('4','4BHK'),
    ('5','5BHK'),
)
class Property(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid1,editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.PositiveIntegerField()   
    image = models.ImageField(upload_to='media/')
    square_foot = models.PositiveIntegerField()
    location = models.CharField(max_length=120)
    bhk = models.CharField(choices=BHK_CHOICE)
    additional_bhk = models.CharField(max_length=50,null=True,blank=True)
    open = models.BooleanField(default=True)
    bought_by = models.ForeignKey(Account,blank=True,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'Property - {self.name} at {self.location[:20]}'
