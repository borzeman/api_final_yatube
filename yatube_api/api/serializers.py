from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework.serializers import CurrentUserDefault, ValidationError
from rest_framework.serializers import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Group, Follow


User = get_user_model()


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'group', 'pub_date')
        model = Post


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'post', 'created', 'author')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(ModelSerializer):
    user = StringRelatedField(
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        read_only=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('id', 'following', 'user')
        model = Follow
        read_only_fields = ('user',)
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following']
        )]

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user if request else None
        following = attrs.get('following')
        if user == following:
            raise ValidationError('Подписка на себя невозможна')
        return attrs
