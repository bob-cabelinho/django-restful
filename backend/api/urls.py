from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.api_home),                               # localhost:8000/api/
    path('auth/', obtain_auth_token)                        # localhost:8000/api/auth/
]
