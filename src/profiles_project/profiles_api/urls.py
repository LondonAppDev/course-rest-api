from django.conf.urls import url, include

from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register(
    'hello-viewset', views.HelloViewSet, base_name="hello-view-set")

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'^token/', views.LoginView.as_view()),
    url(r'', include(router.urls)),
]
