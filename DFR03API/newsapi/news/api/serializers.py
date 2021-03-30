from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist



class JournalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    author = JournalistSerializer()

    class Meta:
        model = Article
        # It has 3 ways to implement it.
        # fields = "__all__" # We want all the fields of the model
        # fields = ("title", "description", "boady") # Selecting which one if the fields will choose.
        exclude = ("id",)

    def get_time_since_publication(self, object):
        publication_data = object.publication_data
        now = datetime.now()
        time_delta = timesince(publication_data, now)
        return time_delta

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and Description must be different from each other"
            )
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError(
                "Title must be at least 30 characters long"
            )
        return value


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
            "publication_data", instance.publication_data
        )
        instance.active = validated_data.get("active", instance.description)

        instance.save()

        return instance

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and Description must be different from each other")
        return data
    
    def validate_title(self, value):
        if len(value) <60:
            raise serializers.ValidationError("Title must be at least 60 characters long")
        return value
"""
