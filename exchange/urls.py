from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('recensement-page/', views.recensementPage, name="recensement-page"),
    path('recensement-validation/', views.recensementValidation, name="recensement-validation"),
    path('update-validation/<int:id>', views.updateValidation, name="update-validation"),
    path('news-file', views.newsFile, name="news-file"),
    path('prestation-form', views.prestationForm, name="prestation-form"),
    path('notification/', views.notification, name="notification"),
    path('projects', views.projectsRoom, name="projects"),
    path('health', views.healthRoom, name="health"),
    path('create-community', views.createCommunity, name="create-community"),
    path('community', views.Community, name="community"),
    path('center-interest', views.centerInterest, name="center-interest"),
    path('posts', views.Posts, name="posts"),
    path('create-project', views.createProjects, name="create-project"),
    path('buisness-space', views.buisnessSpace, name="buisness-space"),
    path('job-offer', views.jobOffer, name="job-offer"),
    path('rom-health', views.romHealth, name="rom-health"),
    path('consultation-health', views.consultationHealth, name="consultation-health"),
    path('census', views.census, name="census"),
    path('info-page', views.infoPage, name="info-page"),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)