from django.conf.urls import url, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^token/', views.LoginView.as_view()),
]
