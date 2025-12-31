
from django.urls import path,path,include
from.views import add_to_card,show_my_cart,decrease_item,delete_item
urlpatterns = [
   
    path('decrease_item/<int:pk>',decrease_item,name='decrease_item'),
    path('add_to_card/<int:pk>',add_to_card,name='add_to_card'),
    path('delete_item/<int:pk>',delete_item,name='delete_item'),



    path('show_my_cart/',show_my_cart,name='show_my_cart'),
   
   

   
]
