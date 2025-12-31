


from django.urls import path
from .views import maek_order,go_for_payment,order_detials_form

urlpatterns = [
    
path('maek_order/', maek_order,name='maek_order'),
path('go_for_payment/', go_for_payment,name='go_for_payment'),
path('order_detials_form/<int:pk>/', order_detials_form,name='order_detials_form'),

 
]
