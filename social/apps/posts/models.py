from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120, null=False)
    text = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=False)

    def __str__(self):
        return f'PostUserID:{self.pk}. PostTitle:{self.title} - PostUser:{self.user}'

    def likes_number(self):
        return self.likes.count()


class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'post', )

    def __str__(self):
        return f'UserLikeID:{self.pk}. PostInfo:{self.post} - UserLike:{self.user}'
