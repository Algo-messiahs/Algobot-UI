from django.urls import path
from django.contrib.auth.views import login_required
from django.contrib.auth import views as auth_views
from . import views

app_name = 'algobot'
urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path(r'login/$', login_required, {'template_name': 'account/login.html'}),
]
