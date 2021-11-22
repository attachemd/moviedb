from rest_framework import serializers

from core.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = ['id', 'name', 'about', 'website', 'active']
        fields = '__all__'

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     about = serializers.CharField()
#     website = serializers.URLField()
#     active = serializers.BooleanField()
#
#     # def validate_name(self, value):
#     #     """
#     #     Check that the blog post is about Django.
#     #     """
#     #     if not value:
#     #         raise serializers.ValidationError("The name field is empty.")
#     #     return value
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.about = validated_data.get('about', instance.about)
#         instance.active = validated_data.get('active', instance.active)
#         instance.website = validated_data.get('website', instance.website)
#         instance.save()
#         return instance
