from django.db import models
from store.models import Food
from django.contrib.auth.models import User


# Create your models here.


class Reviews(models.Model):
     food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='reviews')
     
     discription = models.TextField()
     RATING_CHOICES = (
        (1, '1 out of 5'),
        (2, '2 out of 5'),
        (3, '3 out of 5'),
        (4, '4 out of 5'),
        (5, '5 out of 5'),)
     rating = models.IntegerField(choices=RATING_CHOICES)
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add = True)

     class Meta:
        
        unique_together = (('food', 'user'),)

