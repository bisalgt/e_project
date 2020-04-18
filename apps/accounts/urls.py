
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from apps.accounts.views import SignUpView, user_detail, user_update, user_delete, my_profile

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:id>/<str:slug>/", user_detail, name="user_detail"),
    path("<int:id>/<str:slug>/my_profile/", my_profile, name="my_profile"),
    path("<int:id>/<str:slug>/update/", user_update, name="user_update"),
    path("<int:id>/<str:slug>/delete/", user_delete, name="user_delete"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('success/', TemplateView.as_view(template_name='accounts/success.html'), name='success'),
]
