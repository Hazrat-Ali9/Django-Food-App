
from django.urls import path,path,include
from.views import see_user_ordr_history,sign_up,log_in,log_out,user_profile,change_password,profileUP,verify,send_varificatoin_email
from django.contrib.auth import views as auth_views
urlpatterns = [
   
    path('sign_up/',sign_up,name='sign_up'),
    path('change_password/',change_password,name='change_password'),
    path('login/',log_in,name='login'),
    path('log_out/',log_out,name='log_out'),
    path('user_profile/',user_profile,name='user_profile'),
    path('profileUP/',profileUP,name='profileUP'),
    path('see_user_ordr_history/',see_user_ordr_history,name='see_user_ordr_history'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('send_varificatoin_email/' , send_varificatoin_email , name="send_varificatoin_email"),

   


   path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),




    
]
