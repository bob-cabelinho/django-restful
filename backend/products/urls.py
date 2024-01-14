from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductListCreateAPIView.as_view()),                 # localhost:8000/products/
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),            # localhost:8000/products/<int:pk>
    path("<int:pk>/update/", views.ProductUpdateAPIView.as_view()),     # localhost:8000/products/<int:pk>/delete/
    path("<int:pk>/delete/", views.ProductDeleteAPIView.as_view())      # localhost:8000/products/<int:pk>/update/
]
