"""aleteia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from django.urls import include, path  # For django versions from 2.0 and up

admin.site.site_header = 'Aleteia'

schema_view = get_swagger_view(title='Aleteia API')

urlpatterns = [
        url(r'^$', schema_view),
        url(r'^admin/', admin.site.urls),
        url(r'^api/v1/', include('api.urls')),
        url(r'^i18n/', include('django.conf.urls.i18n')),
        url(r'^jet', include('jet.urls')),
    ]
