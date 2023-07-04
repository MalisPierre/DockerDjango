from django.db.models import fields
from rest_framework import serializers
from .models import FilmCateg, Film
 
class FilmCategSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCateg
        fields = ('title', 'description')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'description', 'categs', 'publish_date')