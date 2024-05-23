from main import views as mainViews
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

def decide_show_or_login(request):
    if request.user.is_authenticated:
        return redirect('show')
    else:
        return redirect('loginaccount')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',mainViews.home,name='home'),
    path('show/',mainViews.show,name='show'),
    path('Links/',include('Links.urls')),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('', decide_show_or_login),
    
]

urlpatterns += static(settings.MEDIA_URL, 
 document_root=settings.MEDIA_ROOT)
