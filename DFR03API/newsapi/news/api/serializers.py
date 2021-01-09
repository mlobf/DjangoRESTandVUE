from rest_framework import serializers
from news.models import Article

"""
    How it work's
        Deserialization
            1- Parse stream in to python native data type
"""


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    boady = serializers.CharField()
    location = serializers.CharField()
    publication_data = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)

        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description)
        instance.boady = validated_data.get("body", instance.boady)
        instance.location = validated_data.get("location", instance.location)
        instance.publication_data = validated_data.get(
            "publication_date", instance.publication_date
        )
        instance.active = validated_data.get("active", instance.description)

        instance.save()

        return instance
