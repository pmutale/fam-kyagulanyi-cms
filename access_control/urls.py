from django.conf.urls import url

from access_control.views import LoginView, UserCreate

urlpatterns = [
    url(r"^create/", UserCreate.as_view(), name="user_create"),
    url(r"^login/", LoginView.as_view(), name="user_login")
]
