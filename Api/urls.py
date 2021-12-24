from django.urls import path

from Api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('alphabet/', views.alphabets, name='Alphabet'),
    path('word/', views.words, name="Word"),
    path('get-video/', views.getVideo, name="Get-Video"),
]
