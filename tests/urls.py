from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path('private/', views.PrivateView.as_view(), name="private"),
    path('secret/', views.SecretView.as_view(), name="secret"),
]