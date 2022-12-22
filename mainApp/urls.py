from django.urls import path, include, re_path
from rest_framework import routers 
from .views import UserViewSet
from mainApp import views
#routes the data to be viewed from the db
router = routers.DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
urlpatterns += [
    # signup page
    path('signup/', views.signup_view, name='signup'),
    # login page
    path('login/', views.login_view, name='login'),
    # logout page
    path('logout/', views.logout_view, name='logout'),
    # user profile edit page
    path('profile/', views.profile_view, name='profile'),
]