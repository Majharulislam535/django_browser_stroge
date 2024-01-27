from django.urls import path
from .import views
urlpatterns = [
    path('', views.set_session,name='home'),
    path('get/', views.get_cookie),
    path('del/', views.delete_cookie),
    path('get_session/',views.get_session),
    path('delete_session/',views.delete_session)
    
]