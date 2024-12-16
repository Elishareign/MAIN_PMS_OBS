from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import debug_toolbar
from django.contrib import admin

"""
URL configuration for PMS_INTEGRATION project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('_debug_/', include(debug_toolbar.urls)),
    path('', include('rooms.urls')),
    path('', include('hoome.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)