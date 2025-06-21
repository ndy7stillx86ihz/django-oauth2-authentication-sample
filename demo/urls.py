from django.urls import path
from . import views
from demo.views import PageView, HomeView, CallbackView, WelcomeView

app_name = 'demo'

# TODO: cambiar las cosas de auth, para /auth/...
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('callback', CallbackView.as_view(), name='callback'),
    path('login', views.github_login, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('page', PageView.as_view(), name='page'),
]
