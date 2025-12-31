from django.shortcuts import render,redirect
from store.models import Food
from cart.models import Cart_item
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_to_card(request,pk):
    if request.user.is_authenticated:
       user = request.user
       product = Food.objects.get(pk=pk)
       card_item = Cart_item.objects.filter(food=product,user=user,done=False).exists()
       if card_item:
            item = Cart_item.objects.get(food=product,user=user)
            item.quantity+=1
            item.save()
       else:
           item = Cart_item.objects.create(food=product,user=user,quantity=1)
           item.save()
        
       return redirect('show_my_cart') 
           
    else:
        return redirect('sign_up')


@login_required
def delete_item(request,pk):

    if request.user.is_authenticated:
       user = request.user
       product = Food.objects.get(pk=pk)
       card_item = Cart_item.objects.filter(food=product,user=user)
       if card_item:
            item = Cart_item.objects.get(food=product,user=user)
        
            item.delete()
       
       return redirect('show_my_cart') 
           

    else:
        return redirect('sign_up')

@login_required
def decrease_item(request,pk):
     
     if request.user.is_authenticated:
       user = request.user
       product = Food.objects.get(pk=pk)
       card_item = Cart_item.objects.filter(food=product,user=user)
       if card_item:
            item = Cart_item.objects.get(food=product,user=user)
            item.quantity-=1
            item.save()
            if item.quantity<1:
                item.delete()
       
       return redirect('show_my_cart') 
           

     else:
        return redirect('sign_up')
     

@login_required
def show_my_cart(request):

    if request.user.is_authenticated:
            all_items = Cart_item.objects.filter(user=request.user,done=False)

            sub_total = 0
            delivery_cost = 10
            for i in all_items :sub_total += i.sub_stotal()
            total =  sub_total+ delivery_cost
            return render (request,'cart.html',{"all_items":all_items,'total':total,'sub_total':sub_total,'delivery_cost':delivery_cost  })
    
    
    else:
        return redirect('sign_up')