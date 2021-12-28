from django.urls import path

from Api import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('alphabet/', views.alphabets, name='Alphabet'),
    path('word/', views.words, name="Word"),
    path('get-video/', views.getVideo, name="Get-Video"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)