from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from backend import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('search-log/', views.search_log),
    path('inbox/', views.inbox),
    path('manual-agents/', views.manual_agents),
    path('referrals/', views.referrals),
    path('agent-profiles/', views.profile),
    path('messages/', views.messages),
    path('admin/', views.admin),
    path('update-profile/', views.update_profile),
    path('settings/', views.settings),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
