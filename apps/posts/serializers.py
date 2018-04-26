from rest_framework.serializers import ModelSerializer

from apps.posts.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # import ipdb
        # ipdb.set_trace()
        fields = (
            'id', 'title', 'slug', 'image', 'height_field', 'width_field', 'content', 'draft', 'publish', 'read_time',
            'updated', 'timestamp', 'author', 'future_post', 'tag_list', 'tag_count')

    # def get_queryset(self, request):
    #     return super(PostSerializer, self).get_queryset(request).prefetch_related('tags')
    #
    # def tag_list(self, obj):
    #     return u", ".join(o.name for o in obj.tags.all())
