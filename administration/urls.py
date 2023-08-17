from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin-home', views.adminHome, name="admin-home"),
    path('dynamism-list', views.dynamism, name="dynamism-list"),
    path('demography', views.demography, name="demography"),
    path('project-list', views.project, name="project-list"),
    path('project-form', views.projectForm, name="project-form"),
    path('project-detail', views.project, name="project-detail"),
    path('markaz', views.markaz, name="markaz"),
    path('markaz-form', views.markazForm, name="markaz-form"),
    path('file-consultation', views.healthConsultation, name="file-consultation"),
    path('health-data', views.healthData, name="health-data"),
]