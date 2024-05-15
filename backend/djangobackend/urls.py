from django.contrib import admin
from django.urls import path,include
from djangobackend import views
from djangobackend import NewViews

urlpatterns = [
    path('getAnyInformation',views.Order_Product),
    path('pass',NewViews.Excute)
]