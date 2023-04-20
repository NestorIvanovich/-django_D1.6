from django.urls import path
from . import views  # поиск модуля в текущей директории


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home')
]