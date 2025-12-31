from django.db import models
from django.contrib.auth.models import User
from store.models import Food
from order. models import Order
# Create your models here.
class Cart_item(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     food= models.ForeignKey(Food,on_delete=models.CASCADE)
     order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='item')
     quantity=models.IntegerField()
     done = models.BooleanField(default = False)

     def sub_stotal(self):
          if  self.food.dis_count_availave:
                return self.quantity*self.food.price_after_discout()
          else:    
           return self.quantity*self.food.price

     def __str__(self) -> str:
          return self.food.food_name