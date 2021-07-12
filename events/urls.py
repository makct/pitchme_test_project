from django.urls import path

from . import views


app_name = "events"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home_page, name="home"),
    path("search_result/", views.search_result, name="search_result"),
    path("search/", views.search, name="search"),
    path(
        "repeat_search_request/<int:history_log_id>/",
        views.repeat_search_request,
        name="repeat_search_request",
    ),
]
