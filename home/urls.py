from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path("", views.MainView.as_view(), name="main"),
    path("criteria/", views.CriteriaView.as_view(), name="criteria"),
]
