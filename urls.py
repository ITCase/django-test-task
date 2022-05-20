# Copyright 2022 ITCase (info@itcase.pro)

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView

from filebrowser.sites import site as fb_site
from rest_framework.authtoken import views as rest_token_views

admin.autodiscover()

urlpatterns = [
    # admin
    path(
        'admin/',
        include([
            # third-party
            path('django-rq/', include('django_rq.urls')),
            path('filebrowser/', fb_site.urls),
            path('grappelli/', include('grappelli.urls')),

            # django
            path('', admin.site.urls),
        ])),

    # rest
    path('rest/',
         include([
             path('token/', rest_token_views.obtain_auth_token),
         ])),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
