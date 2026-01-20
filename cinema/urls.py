from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cinema.views import GenreViewSet

router = SimpleRouter()
router.register("genres", GenreViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls))
]
