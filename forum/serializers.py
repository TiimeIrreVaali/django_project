from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    comments_number = serializers.SerializerMethodField()
    class Meta:
        model = Topic
        fields = '__all__'

    def get_comments_number(self, obj):
        num = len(Comment.objects.filter(topic__id=obj.id))
        return num


class CommentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    topic_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = Comment
        fields = '__all__'