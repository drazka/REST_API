

from rest_framework import serializers

from movies.models import Person, Movie, Role


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')

    class Meta:
        model = Role
        fields = ('id', 'name', 'role', )


class MovieSerializer(serializers.ModelSerializer):
    role_in_movie = RoleSerializer(source='role_set', many=True)

    director_id = serializers.IntegerField(source='director.id')
    director_name = serializers.CharField(source='director.name')

    class Meta:
        model = Movie
        fields = ('title', 'description', 'director_id', 'director_name', 'role_in_movie', 'year' )