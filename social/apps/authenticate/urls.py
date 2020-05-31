from django.conf.urls import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from apps.posts.views import UserLikeListByDay

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


api_urlpatterns = [path('accounts/', include('rest_registration.api.urls')),]

urlpatterns = [
    path('', views.api_root, name='api-root'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('groups/', views.GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='group-detail'),

    path('api/v1/', include(api_urlpatterns)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/analitics/', UserLikeListByDay.as_view(), name='user_like_list_by_day'),

    path('users/<int:pk>/activity', views.UserActivityDetail.as_view(), name='user-activity-detail'),

    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
