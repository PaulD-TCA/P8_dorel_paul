from django.urls import path

from . import views

urlpatterns = [
    # path('', views.search, name='search'),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('results_page/', views.results, name='results_page'),
    path('food_page/<int:id>/', views.food_page, name='food_page'),
    path('save_page/<int:id>/', views.save_page, name='save_page'),
    path('my_favourites_page/', views.my_favourites, name='my_favourites_page'),
    # path('', views.account, name='account'),
]

# from django.conf.urls import url
#
# from . import views
#
#
# urlpatterns = [
#     url(r'^$', views.index),
#     # url(r'^(?P<album_id>[0-9]+)/$', views.detail),
#     # url(r'^search/$', views.search),
# ]
