from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    foto = serializers.ImageField(use_url=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'foto',
            'created_at'
        )
        read_only_fields = ('created_at',)