from django.shortcuts import render,redirect
from.models import Food,Category
from review .models import Reviews
from django.core.paginator import Paginator
# Create your views here.


# functon for searchr

def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        all_food = Food.objects.filter(food_name__contains=search_query)
        page = request.GET.get('page')
        paginator = Paginator( all_food, 4)
        all_food_for_page = paginator.get_page(page)
        
    
    else:
        
        page = request.GET.get('page')
        search_query = request.GET.get('search_query')
        
        all_food = Food.objects.filter(food_name__contains=search_query)
        paginator = Paginator( all_food, 4)
        all_food_for_page = paginator.get_page(page)

    if all_food.count()==0: return render(request,'noitemfound.html')
    catagories = Category.objects.all()
    return render(request,'search_item.html',{'items':all_food_for_page,'catagories':catagories,'search_query':search_query})
    




def pro_detials(request,pk):
    yes_ase = Food.objects.filter(pk=pk).exists()
    if yes_ase:
       food =  Food.objects.get(pk=pk)
       all_reviews = Reviews.objects.filter(food=food)
       return render(request,'food.diteals.html',{'food':food,'all_reviews':all_reviews})
    return redirect('home')



def dicout_page(request):
    
    all_food = Food.objects.filter(dis_count_availave=True)
    if all_food.count()<=0:
        return render(request,'nodiscount.html')
    catagories = Category.objects.all()
    print(type(all_food))
    return render(request,'index.html',{'items':all_food,'catagories': catagories})