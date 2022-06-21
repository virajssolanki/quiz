from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
# from django.contrib.auth.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls')),
    path("auth/", include("django.contrib.auth.urls")),
    path('', include('quiz.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    