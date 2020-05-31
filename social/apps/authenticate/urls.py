from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from apps.posts.views import UserLikeListByDay


api_urlpatterns = [path('accounts/', include('rest_registration.api.urls')),]

urlpatterns = [
    path('', views.api_root),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('groups/', views.GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),

    path('api/v1/', include(api_urlpatterns)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/analitics/', UserLikeListByDay.as_view(), name='user_like_list_by_day'),

    path('users/<int:pk>/activity', views.UserActivityDetail.as_view(), name='user-activity-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
