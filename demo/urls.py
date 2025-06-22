from django.urls import path

from demo.views import PageView, HomeView, WelcomeView

app_name = 'demo'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('page', PageView.as_view(), name='page'),
]
