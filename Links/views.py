
from django.shortcuts import render,redirect,get_object_or_404
from . models import Links,Category, UserProfile
from django.contrib.auth.decorators import login_required
import os
import re
from xhtml2pdf import pisa  
from django.http import HttpResponse
from django.template.loader import render_to_string
from bs4 import BeautifulSoup
import requests

# Create your views here

@login_required
def index(request):
    return render(request, 'index.html', {'data': data})

@login_required
def webpage(request):
    category=request.GET.get('category')
    if category==None:
        pages=Links.objects.all()
    else:
        pages=Links.objects.filter(category__category=category)
    categorys=Category.objects.all()
    return render(request,'webpage.html',{'pages':pages,'categorys':categorys})

@login_required
def adddata(request):  
    if request.method == "POST":
        media = request.POST.get('media')
        type = request.POST.get('type')
        industry = request.POST.get('industry')
        audience = request.POST.get('audience')
        visting = request.POST.get('visting')
        action = request.POST.get('action')
        cost=request.POST.get('cost')
        category = request.POST.get('category')  
        category_obj = Category.objects.filter(pk=category).first()

        if len(request.FILES) != 0:
            logo = request.FILES['logo']

        prod = Links(
            logo=logo,media=media,type=type,industry=industry,audience=audience,
            visting=visting,action=action,cost=cost,category=category_obj
        )

        prod.save()
    
        return redirect('mediass')
    categories = Category.objects.all()    
    return render(request, 'adddata.html', { "categories": categories })

@login_required
def addcategory(request):
    if request.method=='POST':
        category=request.POST.get('category')
        price=request.POST.get('price')
        cat=Category(
            category=category,
            price=price
        )
        cat.save()
        return redirect('/')
    return render(request, 'addcategory.html')

@login_required
def mediass(request):
    pages = Links.objects.all()

    adjusted_links = []
    for page in pages:
        user = request.user
        if not user.is_superuser:  
            adjusted_cost = page.calculate_final_price(user)
        else:
            adjusted_cost = page.cost
        adjusted_links.append({'page': page, 'adjusted_cost': adjusted_cost})

    cats = Category.objects.all()
    adjusted_cate = []
    for cat in cats:
        user = request.user
        if not user.is_superuser:  
            adjusted_price = cat.calculate_final_price(user)
        else:
            adjusted_price = cat.price
        adjusted_cate.append({'cat': cat, 'adjusted_price': adjusted_price})

    return render(request, 'mediass.html', {
        'pages': pages,
        'categories': cats,
        'adjusted_links': adjusted_links,
        'adjusted_cate': adjusted_cate
    })

@login_required
def cate(request):
    cats=Category.objects.all()
    adjusted_cate = []
    for cat in cats:
        user = request.user
        if not user.is_superuser:  
            adjusted_price = cat.calculate_final_price(user)
        else:
            adjusted_price = cat.price
        adjusted_cate.append({'cat': cat, 'adjusted_price': adjusted_price})
    return render(request,'cate.html',{'cat':cat,'adjusted_cate': adjusted_cate})

@login_required
def deletemedia(request,id):
    medias=get_object_or_404(Links,id=id)
    medias.delete()
    return redirect('mediass')

@login_required
def deletecategory(request,id):
    category=get_object_or_404(Category,id=id)
    category.delete()
    return redirect('mediass')

@login_required
def updatemedia(request,pk):
    prob=Links.objects.get(id=pk)
    if request.method=="POST":
        if len(request.FILES) != 0:
            if len(prob.logo)>0:
                os.remove(prob.logo.path)
            prob.logo=request.FILES['logo']
        prob.media = request.POST.get('media')
        prob.type = request.POST.get('type')
        prob.industry = request.POST.get('industry')
        prob.audience = request.POST.get('audience')
        prob.visting = request.POST.get('visting')
        prob.cost = request.POST.get('cost')
        prob.action = request.POST.get('url')
        prob.save()
        return redirect('mediass')  
    context={'prob':prob}
    return render(request,'updatemedia.html',context)

@login_required
def updatecategory(request,pk):
    prob=Category.objects.get(id=pk)
    if request.method=="POST":
        prob.category=request.POST.get('category')
        prob.price=request.POST.get('price')
        prob.save()
        return redirect('mediass')
    context={'prob':prob}
    return render(request,'updatecategory.html',context)

@login_required
def plan(request):
    user = request.user
    if not user.is_superuser: 
        user_profile = UserProfile.objects.get(user=user)
        package = user_profile.package
        return render(request,'plan.html',{'package':package})
    else:
        return render(request,'plan.html')


@login_required
def createurl(request):
    if request.user.is_authenticated:
        categorys = Category.objects.filter(user=request.user)
    if request.method=='POST':
        global res
        res=request.POST.get('url')
        global content
        content=request.POST.get('content')
        global gory
        gory=request.POST.get('drop')
        u = res.split("/")[-2]
        global data1
        data1=Links.objects.filter(category__category=gory)
        url=data1.order_by('-audience').values_list('action',flat=True)
        global data
        if url:
            data=[str(i) + '/' + u   for i in url]
        return render(request,'createurl.html',{'data':data,'content':content,'categorys':categorys})
    else:
        return render(request,'createurl.html',{'categorys':categorys})

@login_required
def generate_pdf(request):
    #web scraping
    pr=requests.get(res)
    soup=BeautifulSoup(pr.text,'html.parser')
    title=soup.find('h1',class_='tdb-title-text')
    date=soup.find('div',class_='td_block_wrap tdb_single_date tdi_99 td-pb-border-top td_block_template_1 tdb-post-meta').getText().strip()
    div_with_p = soup.find('div', class_='td_block_wrap tdb_single_content tdi_104 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
    if div_with_p:
        all_p_tags = soup.find_all('p')

        if all_p_tags:
            text_list = []
            for p_tag in all_p_tags:
                # Extract the text content of each <p> tag
                p_text = p_tag.getText()
                text_list.append(p_text)
            combined_text = '\n'.join(text_list)
    substrings_to_remove = ["Date:","Log in to leave a comment", "Share post:", "Popular","© 2024 | All Rights Reserved.","The Leading Digital PR Distribution Agency – InfluencersPro"]
    # Replace each substring with an empty string
    for substring in substrings_to_remove:
        combined_text = combined_text.replace(substring, "")
    title_text = title.getText().strip() if title else "Title not found"
    match = re.search(r'\.tdb-featured-image-bg\s*\{.*?background:url\(\'(.*?)\'\)',pr.text)
    if match:
        image_url = match.group(1)
    else:
        image_url = None
    #get potenial data
    pd=data1.values_list('audience',flat=True)
    numbers_only = [int(re.search(r'\d+', item).group()) for item in pd]
    total = sum(numbers_only)
    total_sum_int = total / 10000.0 
    total_sum = "{:.2f}".format(total_sum_int)
    logo = data1.order_by('-audience')[:6].values_list('logo')    

    # Step 1: Query Database
    db_data =data1.order_by('-audience').values_list('logo','media', 'type', 'industry', 'visting', 'audience')
    # Step 2: Generate Temporary Data
    temp_data = data
    # Step 3: Combine Data
    combined_data = []
    for db_row, temp in zip(db_data, temp_data):
        combined_data.append([*db_row, temp])
    length=len(combined_data)
    print("\n",length,"\n")

    # Step 4: Pass Combined Data to Template
    html = render_to_string('index.html', {'combined_data': combined_data,"logo":logo,
                                           'title': title_text,'length':length,
                                          'date':date,'combined_text':combined_text,
                                          'gory':gory,'total_sum':total_sum,
                                          "image_url":image_url})
    
    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Report.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors')
    return response