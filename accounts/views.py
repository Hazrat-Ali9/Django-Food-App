from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import User_profile_update
from order.models import Order


from.models import Profile


import uuid
from django.conf import settings
from django.core.mail import send_mail

#from django.contrib.sites.models import Site
# Create your views here.







def sign_up(request):
    if request.method=="POST":
         form = RegistrationForm(request.POST) 
         email = request.POST.get('email')
         yes_have_with_email = User.objects.filter(email=email).exists()
         if yes_have_with_email:
            print('yes have ')
            messages.error(request, 'a user already  exists with thid email')
           
             


         if form.is_valid() and not  yes_have_with_email:
             user = form.save()
             login(request,user)
             auth_token = str(uuid.uuid4())
             Profile.objects.create(user = user , auth_token = auth_token)
             send_mail_after_registration(email ,auth_token,)
             return render(request,'emilcheck.html')
         
         else:
            messages.error(request, 'in valied form ')
            return redirect('sign_up')
    else:
        form = RegistrationForm()    
    return render (request,'register.html',{'form':form})








def log_in(request):
   if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       print(request.POST)
       user = authenticate(username= username, password= password)
       if user is not None:
           login(request,user)
           return redirect('user_profile')

   return render(request,'login.html')


@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    return render(request,'profile.html')


@login_required
def profileUP(request):
    if request.method == 'POST':
        user_form = User_profile_update(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
         
            messages.success(request, 'Your profile is updated successfully')
            return redirect('user_profile')
    else:
        user_form = User_profile_update(instance=request.user)
       
    return render(request, 'profile_p.html', {'form': user_form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass.html', {
        'form': form
    })



@login_required
def see_user_ordr_history(request):
    my_orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request,'hostory.html',{'my_orders':my_orders})









def verify(request,auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('user_profile')
        else:
            messages.success(request, 'no user found ')
            return redirect('login')
    except Exception as e:
         messages.success(request, 'errors occers')
         return redirect('login')







def send_mail_after_registration(email,token ):
    

    subject = 'Your account needs to be verified'
    message = f'Hi, please click the following link to verify your account: https://food-site-03s7.onrender.com/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, email_from, recipient_list)








@login_required
def send_varificatoin_email(request):
     auth_token = str(uuid.uuid4())
     try:
       profile =  Profile.objects.get(user=request.user)
       profile.auth_token=auth_token
     except Exception as e:
        profile =  Profile.objects.create(user = request.user , auth_token = auth_token)
         
     profile.save()
     send_mail_after_registration(request.user.email,auth_token)
     return render(request,'emilcheck.html')
    
