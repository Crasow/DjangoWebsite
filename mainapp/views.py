from typing import Any, Dict
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from mainapp import models



class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_qs"] = models.News.objects.all()[:5]
        return context

class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"
    
    def get_context_data(self, pk=None, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(pk = pk, **kwargs)
        context["news_objects"] = get_object_or_404(models.News, pk=pk)
        return context

class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = models.Courses.objects.all()[:7]
        return context
    
class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"
    
    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(models.Courses, pk=pk)
        context["lessons"] = models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = models.CourseTeachers.objects.filter(course=context["course_object"])
        return context

class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
