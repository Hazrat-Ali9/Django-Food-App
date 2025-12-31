from django.contrib import admin
from.models import Category,Food
# Register your models here.

class show_cat(admin.ModelAdmin):
    list_display =['category_name']
    prepopulated_fields = {'slug' : ('category_name',)}


class show_food(admin.ModelAdmin):
    prepopulated_fields={'slug':('food_name',)}
    list_display =['food_name','category']


admin.site.register(Category,show_cat)
admin.site.register(Food,show_food)
