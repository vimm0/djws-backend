from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
        'id', 'title', 'slug', 'image', 'height_field', 'width_field', 'content', 'draft', 'publish', 'read_time',
        'updated', 'timestamp', 'author', 'future_post')
