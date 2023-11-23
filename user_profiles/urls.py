# user_profiles/urls.py
from django.urls import path
from .views import user_list, user_detail, create_profile,delete_profile,search_users

urlpatterns = [
    path('', user_list, name='user_list'),
    path('new_profile/', create_profile, name='create_profile'),
    path('details/<int:user_id>/', user_detail, name='user_detail'),
    path('delete/<int:user_id>/', delete_profile, name='delete_profile'),
    path('search/', search_users, name='search_users'),

]
