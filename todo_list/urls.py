from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="TODO_Project",
        default_version='v1',
        description="The Todo List API allows users to manage their todo items efficiently. It provides endpoints for creating, retrieving, updating, and deleting todo items.",
      #   terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="raazkushwaha1996@gmail.com"),
        #license=openapi.License(name="BSD License"),
    ),
    public=True,
)


urlpatterns = [
    path('api/todo', views.todo_list),
    path('api/todo/<int:pk>', views.todo_detail),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]