

from rest_framework import serializers

from movies.models import Person


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'