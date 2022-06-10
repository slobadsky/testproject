from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.index,name='app2-index-page'),
    path('login/', views.login_page,name='app2-login-page'),
    path('logout/', views.logout_page,name='app2-logout-page'),
    path('pr/', views.pr_page,name='app2-pr-page'),
]