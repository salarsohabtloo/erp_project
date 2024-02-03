from django.urls import path

from erp_app.views import home
from .views import user_login, user_logout, user_signup, ceo_dashboard, cto_dashboard, pm_dashboard, admin_dashboard

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/', user_signup, name='user_signup'),
    path('ceo_dashboard/', ceo_dashboard, name='ceo_dashboard'),
    path('cto_dashboard/', cto_dashboard, name='cto_dashboard'),
    path('pm_dashboard/', pm_dashboard, name='pm_dashboard'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
]