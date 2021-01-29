from django.urls import path
from home import views

urlpatterns=[
    path('',views.home,name='home'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addcode',views.addcode,name='addcode')
]