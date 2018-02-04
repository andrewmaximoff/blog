from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/<slug>/', views.CategoriesDetailView.as_view(), name='categories_detail'),
    path('post/<slug>/', views.DetailView.as_view(), name='detail'),

]
