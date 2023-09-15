from django.contrib.auth import get_user_model
from django.db import models

STR_LIMIT_TITLE = 21
STR_LIMIT_TEXT = 31

User = get_user_model()


class Group(models.Model):
    '''Модель для групп'''

    title = models.CharField(max_length=256)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title[:STR_LIMIT_TITLE]

    class Meta:
        ordering = ('title',)


class Post(models.Model):
    '''Модель для записей'''

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:STR_LIMIT_TEXT]

    class Meta:
        ordering = ('pub_date',)


class Comment(models.Model):
    '''Модель для комментариев'''

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    def __str__(self):
        return self.created

    class Meta:
        ordering = ('created',)


class Follow(models.Model):
    '''Модель для существующих подписчиков'''

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed', null=True
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers', null=True
    )

    def __str__(self):
        return self.user[:STR_LIMIT_TITLE]

    class Meta:
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            ),
        ]
