from django.urls import path
from app.views import home

# Associate a path to the view
urlpatterns = [
    path("", home),
]