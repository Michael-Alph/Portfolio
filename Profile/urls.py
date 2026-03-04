from django.urls import path
from Profile.views import profile


urlpatterns = [
    path('', profile, name='profile'),
]