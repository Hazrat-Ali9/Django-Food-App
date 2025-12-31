from django.shortcuts import render
from store.models import Food,Category

from django.core.paginator import Paginator
# Create your views here.


def home(request):
    if request.method == 'POST':
        cata = request.POST.get('category')
        catagory = Category.objects.get(category_name=cata)
        all_food_now = Food.objects.filter(category=catagory)

    else:
       all_food_now = Food.objects.all()
    
    catagories = Category.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(all_food_now, 4)
    all_food = paginator.get_page(page)
   
   



    return render(request,'index.html',{'items':all_food,'catagories': catagories})




