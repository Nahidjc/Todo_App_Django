from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
]
