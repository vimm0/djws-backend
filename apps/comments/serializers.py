from rest_framework.serializers import ModelSerializer

from apps.comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('object_id', 'content_type', 'post_name', 'commenter', 'content', 'timestamp')
