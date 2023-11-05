from typing import Any, Dict, Tuple
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class NewsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(models.Model):
    objects = NewsManager()

    title = models.CharField("Title", max_length=256)
    preambule = models.CharField("Preambule", max_length=1024)
    body = models.TextField("Body", null=True, blank=True)
    body_as_markdown = models.BooleanField("As markdown", default=False)
    created = models.DateTimeField("Created", auto_now_add=True, editable=False)
    updated = models.DateTimeField("Updated", auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    def delete(self, **args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created",)


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Course(models.Model):
    objects = CoursesManager()

    name = models.CharField("Name", max_length=256)
    description = models.TextField("Description", blank=True, null=True)
    description_as_markdown = models.BooleanField("As markdown", default=False)
    cost = models.DecimalField("Cost", max_digits=8, decimal_places=2, default=0)
    cover = models.CharField("Cover", max_length=25, default="no_image.svg")
    created = models.DateTimeField("Created", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, **args):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    num = models.PositiveIntegerField("Lesson number")
    title = models.CharField("Name", max_length=256)
    description = models.TextField("Description", blank=True, null=True)
    description_as_markdown = models.BooleanField("As markdown", default=False)
    created = models.DateTimeField("Created", auto_now_add=True, editable=False)
    updated = models.DateTimeField("Edited", auto_now=True, editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")


class CourseTeacher(models.Model):
    course = models.ManyToManyField(Course)
    name_first = models.CharField("Name", max_length=128)
    name_second = models.CharField("Surname", max_length=128)
    day_birth = models.DateTimeField("Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()


class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"), (1, "⭐"))
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_("Course")
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("User")
    )
    feedback = models.TextField(default=_("No feedback"), verbose_name=_("Feedback"))
    rating = models.SmallIntegerField(
        choices=RATING, default=5, verbose_name=_("Rating")
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)


def __str__(self):
    return f"{self.course} ({self.user})"
