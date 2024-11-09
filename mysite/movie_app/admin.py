from django.contrib import admin
from .models import *


class MovieLanguageInline(admin.TabularInline):
    model = MovieLanguages
    extra = 1


class MovieMomentsInline(admin.TabularInline):
    model = Moments
    extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [MovieLanguageInline, MovieMomentsInline]


admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(FavoriteMovie)
admin.site.register(Favorite)
admin.site.register(History)
admin.site.register(Movie, MovieAdmin)


