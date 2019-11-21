from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from users.views import UserJoinView, UserLoginView, UserLogoutView
from contents.views import HomeView, GramAddView

urlpatterns = [
    path("s/a/console/", admin.site.urls),
    path("", HomeView.as_view()),
    path("login/", TemplateView.as_view(template_name="login.html")),
    path("join/", TemplateView.as_view(template_name="join.html")),
    path("api/users/", UserJoinView.as_view()),
    path("api/login/", UserLoginView.as_view()),
    path("api/logout/", UserLogoutView.as_view()),
    path("api/contents/", GramAddView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)