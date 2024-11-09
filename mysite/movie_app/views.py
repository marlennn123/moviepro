
from .serializers import *
from rest_framework import viewsets, generics, status


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorySerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


class MovieDetailViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer


class MovieLanguageViewSet(viewsets.ModelViewSet):
    queryset = MovieLanguages.objects.all()
    serializer_class = MovieLanguagesSerializer

class MomentsViewSet(viewsets.ModelViewSet):
    queryset = Moments.objects.all()
    serializer_class = MomentsSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteMovieViewSet(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMovieSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
