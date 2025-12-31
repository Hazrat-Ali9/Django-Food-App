from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
     category_name = models.CharField(max_length=50,unique=True)
     category_img =models.ImageField(upload_to = 'photos/categories', blank = True)
     slug = models.SlugField(max_length= 100, unique = True,default=None)

     def __str__(self) -> str:
          return self. category_name


class Food(models.Model):
    food_name = models.CharField(max_length=50)
    price = models.IntegerField()
    dis_count_availave = models.BooleanField(default=False,null=True)
    parcentage_of_discount = models.IntegerField(null=True,blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    food_img =models.ImageField(upload_to='photos/foodes')
    descriptons=models.TextField()
    slug = models.SlugField(max_length= 100, unique = True,default=None)
    buyers = models.ManyToManyField(User, related_name='bought_foods',blank = True)
    commentors = models.ManyToManyField(User , related_name='comment_foods',blank = True)

    



    def __str__(self) -> str:
          return self.food_name
    
    def price_after_discout(self):
         pirce = self.price
         if self.dis_count_availave:
              pirce -= (pirce*self.parcentage_of_discount)/100
              pirce = int(pirce)
         return pirce














