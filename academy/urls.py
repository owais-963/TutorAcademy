from django.urls import path
from .views import *

urlpatterns = [
    # Define your URL patterns here
    path('', home, name='home'),
    path('joinUs', joinUs, name='joinUs'),
    path('logIn', logIn, name='login'),
    path('logOut', logOut, name='logOut'),
    path('updateProfile', update, name='update'),
    path('yourRequests', yourReq, name='req'),
    path('profile', profile, name='profile'),
    path('cs', contactUs, name='contactUs'),
    path('apply/<str:id>', apply, name='apply'),

]
