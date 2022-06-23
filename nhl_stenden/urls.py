from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path("", include('main.urls')),
  path('admin/', admin.site.urls),
  path('methods/', include('methods.urls')),
  path('robot/', include('robot.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
