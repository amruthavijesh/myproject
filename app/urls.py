from django.urls import path
from . import views

app_name='app'
urlpatterns = [
    path('', views.index, name='index'),
    path('reg_here/', views.Registration, name='reg_here'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_home/<int:id>/', views.user_home, name='user_home'),
    path('view_user_profile/<int:id>/', views.view_user_profile, name='view_user_profile'),
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('logout/', views.index, name='logout'),
    path('change_password/<int:id>/', views.change_password, name='change_password'),
    ]
