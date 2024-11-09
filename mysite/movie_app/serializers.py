from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status',)


class SimpleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name', 'bio', 'age', 'director_image']


class DirectoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name', 'bio', 'age', 'actor_image']


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video', 'movie']


class MovieLanguagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class RatingSerializer(serializers.ModelSerializer):
    user = SimpleProfileSerializer()
    movie = MovieSimpleSerializer()
    created_date = serializers.DateTimeField('%d-%m-%Y %H-%M')

    class Meta:
        model = Rating
        fields = ['user', 'movie', 'stars', 'parent', 'created_date', ]


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = ['cart', 'created_date', 'movie']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['user', 'created_date', ]


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['user', 'viewed_at', 'movie']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True, many=True)
    avarage_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'movie_time', 'avarage_rating', 'status_movie']

    def get_avarage_rating(self, obj):
        return obj.get_avarage_rating()


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True, read_only=True)
    director = DirectoryDetailSerializer(many=True, read_only=True)
    actor = ActorDetailSerializer(many=True, read_only=True)
    movie_language = MovieLanguagesDetailSerializer(many=True, read_only=True)
    avarage_rating = serializers.SerializerMethodField()
    moments_movie = MomentsSerializer(read_only=True, many=True)
    ratings = RatingSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor',
                  'types', 'movie_time', 'description', 'movie_trailer', 'movie_image',
                  'movie_language', 'avarage_rating', "moments_movie", 'ratings', 'status_movie']

    def get_avarage_rating(self, obj):
        return obj.get_avarage_rating()