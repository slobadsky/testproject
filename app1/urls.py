from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index,name='app1-index-page'),
    path('login/', views.login_page,name='app1-login-page'),
    path('logout/', views.logout_page,name='app1-logout-page'),
    path('pr/', views.pr_page,name='app1-pr-page'),
]