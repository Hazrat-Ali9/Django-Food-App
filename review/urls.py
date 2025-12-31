


from django.urls import path
from .views import give_reviews,edit_my_review,change_review

urlpatterns = [
    
path('give_reviews/<int:pk>', give_reviews,name='give_reviews'),
path('edit_my_review/<int:pk>', edit_my_review,name='edit_my_review'),
path('change_review/<int:pk>', change_review,name='change_review'),


 
]
