from django.urls import path

from . import views


app_name = 'no_covers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
