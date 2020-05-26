from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)',views.search_location,name='search_location')

]