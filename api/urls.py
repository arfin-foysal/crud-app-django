from django.urls import path

from api.views import CreateTodoAPIView, DeleteTodoAPIView, ListTodoAPIView, UpdateTodoAPIView


urlpatterns = [
    path("",ListTodoAPIView.as_view(),name="lang_list"),
    path("create/", CreateTodoAPIView.as_view(),name="lang_create"),
    path("update/<int:pk>/",UpdateTodoAPIView.as_view(),name="update_lang"),
    path("delete/<int:pk>/",DeleteTodoAPIView.as_view(),name="delete_lang")
]