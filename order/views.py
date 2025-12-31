from django.shortcuts import render,redirect
from . models import Order
from cart.models import Cart_item
from.forms import OrderForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

import uuid
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.




@login_required
def maek_order(request):
    if request.user.is_authenticated:
       


       try:
         profile =request.user.profile
       except Exception as e:
          auth_token = str(uuid.uuid4())
          profile =  Profile.objects.create(user = request.user , auth_token = auth_token)
          profile.save()

       if not request.user.profile.is_verified :
               return redirect('send_varificatoin_email')
       
       all_items = Cart_item.objects.filter(user=request.user,done=False) 
       if  all_items.count()==0:return redirect('home')
       sub_total = 0
       delivery_cost = 10
       for i in all_items :
                         sub_total += i.sub_stotal()
                         
       total =  sub_total+ delivery_cost



       if request.method=='POST':
                   
                        
                    form = OrderForm(request.POST)
                    print('helo')

                    all_items = Cart_item.objects.filter(user=request.user,done=False)
                    
                    total =  sub_total+ delivery_cost
                    
                    form.instance.delevary_cost=delivery_cost
                    form.instance. product_price=sub_total
                    form.instance. total =total
                    form.instance.user = request.user
                    if form.is_valid():
                         current_order= form.save()
                         for i in all_items :
                           i.order =  current_order
                           i.done=True
                           i.food.buyers.add(request.user)
                           i.food.save()
                           i.save()

                    return render(request,'tnaku.html')
       
       else:
            
            form = OrderForm()
            return render(request,'place_order.thml',{'sub_total':sub_total,'delivery_cost':delivery_cost,'total': total,'form': form})
    else:
        return redirect('sign_up')
    


@login_required
def go_for_payment(request):
    return redirect('maek_order')




@login_required
def order_detials_form(request,pk):
      current_order = Order.objects.get(pk=pk)
      all_items = current_order.item.all()
      for i in all_items:print(i)
      return render (request,'order_detials.html',{'current_order':current_order,'all_items':all_items})