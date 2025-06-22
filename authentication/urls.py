from django.urls import path
from . import views
from .views import CallbackView

app_name = 'authentication'

urlpatterns = [
    path('callback', CallbackView.as_view(), name='callback'),
    path('login', views.oauth_login, name='login'),
    path('logout', views.logout_request, name='logout'),
]
