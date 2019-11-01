from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls import url 
from django.shortcuts import HttpResponse 
from . import views 
#from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("starter/", views.starter, name="starter"),
    path("combo/", views.combo, name="combo"),
    path("programming/", views.programming, name="programming"),
    path("multi_plot/", views.multi_plot, name="multi_plot"),
    path("products/", views.products, name="products"),
    path("pie/", views.pie, name="pie"),
    path("test_html/", views.test_html, name="test_html"),
    
]