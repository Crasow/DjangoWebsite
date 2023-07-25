from django.http import HttpResponse
from django.views.generic import TemplateView
import random


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # get data from TemplateView
        context = super().get_context_data(**kwargs)
        context["news_titles"] = []
        context["news_preview"] = "Description that attract everyone"
        for el in range(5):
            rand_int = random.randint(1,20)
            context["news_titles"].append(f"The best new title {rand_int}")
        return context

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
