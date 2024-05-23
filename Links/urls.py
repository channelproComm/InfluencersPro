from django.urls import path
from . import views

urlpatterns = [
    path('webpage/',views.webpage,name='webpage'),
    path('adddata/',views.adddata,name='adddata'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('mediass/',views.mediass,name='mediass'),
    path('cate/',views.cate,name='cate'),
    path('deletemedia/<int:id>',views.deletemedia,name='deletemedia'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),
    path('updatemedia/<int:pk>', views.updatemedia, name='updatemedia'),
    path('updatcategory/<int:pk>', views.updatecategory, name='updatecategory'),
    path('createurl', views.createurl, name='createurl'),
    path('plan',views.plan,name='plan'),
    path('generate_pdf',views.generate_pdf,name='generate_pdf'), 
    path('index',views.index,name='index'),
]
