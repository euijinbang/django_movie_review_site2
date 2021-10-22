from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/create/', views.create_comment, name='create_comment'),
    path('<int:pk>/likes/', views.likes, name='likes'),
]
