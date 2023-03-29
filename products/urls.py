from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("products/<product>", views.product_cat, name="productcat"),
    path("signup", views.signup, name="signup"),
]
