from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
    path('lga_score/', views.lga_score, name='lga-score'),
    path('upload_score/', views.upload_score, name='upload-score'),
    path('get_lgas_for_state/', views.get_lgas_for_state, name='get_lgas_for_state'),
    path('get_wards_for_lga/', views.get_wards_for_lga, name='get_wards_for_lga'),
    path('get_polling_units_for_ward/', views.get_polling_units_for_ward, name='get_polling_units_for_ward'),  
]