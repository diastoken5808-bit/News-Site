from django.urls import path
from .views import login_view, register_view , news_list

urlpatterns = [
    path('', news_list, name='news_list'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
