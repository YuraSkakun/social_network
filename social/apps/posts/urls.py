from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:post_id>/', views.PostDetail.as_view(), name='post_detail'),

    path('<int:post_id>/user-likes/', views.UserLikeList.as_view(), name='user_like_list'),
    path('<int:post_id>/user-likes/<int:user_like_id>/', views.UserLikeDetail.as_view(), name='user_like_detail'),
]
