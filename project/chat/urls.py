from .views import login_view, logout_view, home_view,register_view
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),  # Add this line for the root URL
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]