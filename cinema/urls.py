from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cinema.views import(
    GenreViewSet,
    ActorViewSet
)

router = SimpleRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)

app_name = "cinema"

urlpatterns = [
    path("", include(router.urls))
]
