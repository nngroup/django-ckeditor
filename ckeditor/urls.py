from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload/', views.upload, name='ckeditor_upload'),
    url(r'^browse/', views.browse, name='ckeditor_browse'),
]
