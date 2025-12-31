from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from.forms import ReviewForm
from store.models import Food
from .models import Reviews


@login_required
def give_reviews(request, pk=1):
    user = request.user
    current_food = Food.objects.get(pk=pk)
    if user in current_food.commentors.all():return redirect('edit_my_review', pk)
    if request.method == "POST":
        
        form = ReviewForm(request.POST)
        form.instance.user = user
        form.instance.food = current_food
        if form.is_valid():
            form.save()
            current_food.commentors.add(user)
            current_food.save()

            return redirect('home')
        else:
            print(form.errors)  # Print form errors to debug
    else:
        form = ReviewForm()
      
    return render(request, 'reviews.html', {'form': form})



@login_required
def edit_my_review(request,pk):# clicing the food 

      user = request.user
      current_food = Food.objects.get(pk=pk)
      current_review = Reviews.objects.get(food= current_food,user=user)
      if request.method=='POST': 
          form = ReviewForm(request.POST,instance=current_review)
          if form.is_valid():
              form.save()
              return redirect('home')
         

      else:
          form = ReviewForm(instance=current_review)
      return render(request, 'reviews.html', {'form': form})




@login_required
def change_review(request,pk):
   
    current_review = Reviews.objects.get(pk=pk)
    if request.method=='POST': 
          form = ReviewForm(request.POST,instance=current_review)
          if form.is_valid():
              form.save()
              return redirect('home')
         

    else:
          form = ReviewForm(instance=current_review)
    return render(request, 'reviews.html', {'form': form})