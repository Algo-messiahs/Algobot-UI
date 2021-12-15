from django.urls import path
from django.contrib.auth.views import login_required
from django.contrib.auth import views as auth_views
from . import views

app_name = 'algobot'
urlpatterns = [
    path('', views.index, name='index'),
    path('sell_stock',views.sell_stock, name='sell_stock'),
    path('buy_stock',views.buy_stock, name='buy_stock'),
    path('monitor_stock',views.monitor_stock, name='monitor_stock'),
    path('generate_report',views.generate_report, name='generate_report')
    # path('login/', views.login, name='login'),
    # path(r'login/$', login_required, {'template_name': 'account/login.html'}),
]
