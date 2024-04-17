from django.urls import path
from .views import *

urlpatterns = [
    path('pidorboard/', leader_board, name='leadboard'),
    path('addrating/', add_rating, name='addrating'),
    path('ratinghistory/', rating_history, name='ratinghistory'),
    path('orehus/id<int:profile_id>/', user_profile, name='profile'),
    path('orehus/personality/', user_settings, name='personality'),
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),

]


