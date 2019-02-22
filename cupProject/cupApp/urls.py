from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="index"),
    path('times2/<int:multiply>/',views.times2, name='times2'),
    path('total/<int:number>/',views.total, name="total"),
    path('hello/<str:name>/',views.sayHello,name='sayHello'),
    path('newCup',views.newCup,name='newCup'),
    path('allPurchase/',views.allPurchase,name="allPurchase"),
    path('newMaterial/',views.newMaterial,name="slightlyNew"),
]