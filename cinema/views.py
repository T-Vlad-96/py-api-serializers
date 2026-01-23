from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            self.serializer_class = MovieListSerializer
        elif self.action == "retrieve":
            self.serializer_class = MovieRetrieveSerializer
        return self.serializer_class
