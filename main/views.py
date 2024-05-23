from django.shortcuts import render
from Links.models import Links,Category,UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    para=request.GET.get('category')
    category=request.GET.get('category')
    if category==None:
        pages=None
    else:
        pages=Links.objects.filter(category__category=category)
    categorys=Category.objects.all()
    ln=Links.objects.all()
    length=len(ln)
    length1=len(categorys)   
    total_cost=sum(link.cost for link in ln if link.cost is not None)
    return render(request,'show.html',{'pages':pages,'categorys':categorys,
                                       'para':para,'length':length,'length1':length1,
                                       'total_cost':total_cost})

@login_required
def show(request):
    if request.user.is_authenticated:
        user_categories = Category.objects.filter(user=request.user)
        links_for_user_categories = Links.objects.filter(category__in=user_categories).distinct()
    categorys=Category.objects.all()
    ln=Links.objects.all()
    length=len(links_for_user_categories)
    length1=len(user_categories) 
    total_cost=sum(link.cost for link in ln if link.cost is not None)
    total_price=sum(cat.price for cat in categorys if cat.price is not None)
    user_count = User.objects.count()
    silver_user_count = UserProfile.objects.filter(package='silver').count()
    gold_user_count = UserProfile.objects.filter(package='gold').count()
    platinum_user_count = UserProfile.objects.filter(package='platinum').count()
    return render(request,'show.html',{'categorys':categorys,
                                       'length':length,'length1':length1,'total_cost':total_cost,
                                       'total_price':total_price,'user_count':user_count,
                                       'silver_user_count':silver_user_count,
                                       'gold_user_count':gold_user_count,'platinum_user_count':platinum_user_count,
                                       'user_categories': user_categories,
                                        'links_for_user_categories':links_for_user_categories})


    
    