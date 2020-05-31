from django.contrib import admin

# Register your models here.
from .models import Post, UserLike


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)


class UserLikeAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "post",)


admin.site.register(Post, PostAdmin)
admin.site.register(UserLike, UserLikeAdmin)
