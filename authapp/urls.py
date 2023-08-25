from django.urls import path
from authapp import views
from authapp.apps import AuthappConfig

app_name = AuthappConfig.name

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("registration/", views.RegisterView.as_view(), name="register"),
]
