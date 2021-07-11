from django.urls import path

from . import views


app_name = "events"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home_page, name='home'),
    path('search_result/', views.search_result, name='search_result'),
    path('search/', views.search, name='search'),
    # path('save_search_pattern/', views.save_search_pattern, name='save_search_pattern'),
    # path('user_filters/', views.user_filters, name='user_filters'),
    path("repeat_search_request/<int:history_log_id>/", views.repeat_search_request, name="repeat_search_request"),
    # path('', views.IndexView.as_view(), name='index'),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("test/", views.test, name="test")
]
