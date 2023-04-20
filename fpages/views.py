from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'flatpages/page_1.html'
