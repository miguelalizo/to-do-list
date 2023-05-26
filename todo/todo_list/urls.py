from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("delete/<todo_id>", views.delete, name="delete"),
    path("cross_off/<todo_id>", views.cross_off, name="cross_off"),
    path("uncross/<todo_id>", views.uncross, name="uncross"),
    path("edit/<todo_id>", views.edit, name="edit")
]
