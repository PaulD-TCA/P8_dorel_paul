from django.urls import path

from . import views

urlpatterns = [

    # path('', views.tutologin, name='tutologin'),
    # path('', views.tutologin, name='tutologin'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_page, name='register_page'),
    
    # path('', views.index, name='index'),
    # path('', views.index, name='results'),
]
