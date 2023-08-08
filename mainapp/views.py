from django.http import HttpResponse
from django.views.generic import TemplateView
import random
from datetime import datetime


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # get data from TemplateView
        context = super().get_context_data(**kwargs)

        context["news_titles"] = "Loud news headline"
        context["news_preview"] = "Description that attract everyone"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()

        # context["news_titles"] = []
        # for el in range(5):
        #     rand_int = random.randint(1,20)
        #     context["news_titles"].append(f"The best new title {rand_int}")
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context
    

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
