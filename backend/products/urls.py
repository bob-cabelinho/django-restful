from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductMixinView.as_view()),                     # localhost:8000/products/
    path("<int:pk>/", views.ProductMixinView.as_view()),            # localhost:8000/products/<int:pk>
    path("<int:pk>/update/", views.ProductMixinView.as_view()),     # localhost:8000/products/<int:pk>/delete/
    path("<int:pk>/delete/", views.ProductMixinView.as_view())      # localhost:8000/products/<int:pk>/update/
]
