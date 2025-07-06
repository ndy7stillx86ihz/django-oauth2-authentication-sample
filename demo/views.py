from django.views.generic.base import TemplateView


class WelcomeView(TemplateView):
    template_name = 'welcome.html'

# todo: que solo se vea el secreto si se tiene el permiso
class PageView(TemplateView):
    template_name = 'page.html'


class HomeView(TemplateView):
    template_name = 'home.html'
