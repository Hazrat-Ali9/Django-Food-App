from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=12,null=True,blank=True)
    email = models.EmailField(max_length=50,null=True)
    address_line1 = models.TextField(null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    

    created_at = models.DateTimeField(auto_now_add = True)
    delevary_cost = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f" {self.user.username}    "