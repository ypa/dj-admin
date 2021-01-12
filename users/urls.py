from django.urls import path

from .views import register, login, AuthenticatedUser, logout, PermissionAPIView


urlpatterns = [
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("user", AuthenticatedUser.as_view()),
    path("permissions", PermissionAPIView.as_view()),
]
