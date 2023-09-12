from rest_framework import serializers


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = serializers.StringRelatedField()
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        fields = ['text', 'image', 'group']
        model = Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['text', 'image', 'group', 'pub_date', 'author']
        read_only_fields = ['text', 'image', 'group', 'pub_date', 'author']
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    following = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Follow
