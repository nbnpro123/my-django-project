from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('main_list', views.main_list),

    path('list_users', views.list_users),

    path('register', views.register_view),
    path('register/', views.register_view, name='register'),
    path('list_users/', views.list_users, name='list_users'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),

    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]
