from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include("base.urls")),
    path('dashboard/', include("dashboard.urls")),
    
    
    path("__reload__/", include("django_browser_reload.urls")),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
