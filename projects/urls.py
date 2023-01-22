from django.urls import path
from . import views


urlpatterns = [ path('project/<str:new>/',views.project ),
 path('', views.projects )]