from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('guitars/', views.GuitarList.as_view(), name="guitar_list"),
    path('guitars/new/', views.GuitarCreate.as_view(), name="guitar_create"),
    path('guitars/<int:pk>/', views.GuitarDetail.as_view(), name="guitar_detail"),
    path('guitars/<int:pk>/update',views.GuitarUpdate.as_view(), name="guitar_update"),
    path('guitars/<int:pk>/delete',views.GuitarDelete.as_view(), name="guitar_delete"),
    
]
