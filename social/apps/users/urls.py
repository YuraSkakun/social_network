from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileList.as_view(), name='user_profile_list'),
    path('<int:user_profile_id>/', views.UserProfileDetail.as_view(),
         name='user_profile'),

    path('<int:user_profile_id>/addresses/',
         views.UserAddressList.as_view(), name='user_adress_list'),
    path('<int:user_profile_id>/addresses/<int:user_address_id>/',
         views.UserAddressDetail.as_view(), name='user_address'),

    path('<int:user_profile_id>/phones/',
         views.UserPhoneList.as_view(), name='user_phone_list'),
    path('<int:user_profile_id>/phones/<int:user_phone_id>/',
         views.UserPhoneDetail.as_view(), name='user_phone'),
]
