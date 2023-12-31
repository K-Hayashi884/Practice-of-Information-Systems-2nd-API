from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import AuthRegister

router = DefaultRouter()
router.register(r"account", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", AuthRegister.as_view()),
]

print(urlpatterns)
