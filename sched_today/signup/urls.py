from django.urls import path
from . import views

app_name = "signup"

urlpatterns = [
    path('landing_page/', views.landing_page, name="landing_page"),
    path('login/', views.login, name="login"),
    path('create_user/', views.create_user, name="create_user"),
    path('dates/', views.dates, name="dates"),
    path('times/', views.times, name="times"),
]