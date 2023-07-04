from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
            path('Shoes55', views.Shoes55),
            path('cart', views.Cartpage),
            path('Signin', views.Signinpage, name='Signin'),
            path('register', views.Register, name='register'),
            path('LOGIN', views.Userlogin, name='LOGIN'),
            path('logout',views.logOut,name='Out'),
            path('sport',views.Sports,name='sport'),
            path('MensCasual',views.Menc,name='MensCasual'),
            path('MensFormals',views.Menf,name='MensFormals'),
            path('womensc',views.Women,name='womensc'),
            path('wsport',views.Wsport,name='wsport'),
            path('Reg',views.registerUser,name='Reg'),
            path('Spark',views.spark,name='Spark'),
            path('Addidas',views.addidas,name='Addidas'),
            path('Nike',views.nike,name='Nike'),
            path('Redtape',views.redtape,name='Reatape'),  
            
    ]