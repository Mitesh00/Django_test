from django.urls import path
from educator import views

urlpatterns = [
    path("",views.ListEducatorAPIView.as_view(),name="educator_list"),
    path("create/", views.CreateEducatorAPIView.as_view(),name="educator_create"),
    path("update/<int:pk>/",views.UpdateEducatorAPIView.as_view(),name="update_educator"),
    path("delete/<int:pk>/",views.DeleteEducatorAPIView.as_view(),name="delete_educator")
]