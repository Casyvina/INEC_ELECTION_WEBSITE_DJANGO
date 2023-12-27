from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
    path('lga_score/', views.lga_score, name='lga-score'),
    path('upload_score/', views.upload_score, name='upload-score'),
    
]