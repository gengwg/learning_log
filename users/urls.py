"""Define URL patterns for the users app."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include the default auth URLs
    path('', include('django.contrib.auth.urls')),
]