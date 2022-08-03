from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='index'),

    path('internship',views.internship,name='internship'),
    path('civilworks',views.civilworks,name='civilworks'),
    path('gallery',views.gallery,name='gallery'),
    path('contactus',views.contactus,name='contactus'),
    path('work_updates',views.work_updates,name='work_updates'),
    path('our_products',views.our_products,name='our_products'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('checkout',views.checkout,name='checkout'),
    path('ButabondSBR_moreinfo',views.ButabondSBR_moreinfo,name='ButabondSBR_moreinfo'),
    
]