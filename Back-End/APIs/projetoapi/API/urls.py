from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'login/', views.Login.as_view()),
    path(r'listar/', views.ListUser.as_view()),
    path(r'criar/', views.CreateUser.as_view()),
    path(r'atualizar/<int:pk>/', views.UpdateUser.as_view()),
    path(r'apagar/<int:pk>/', views.DestroyUser.as_view()),
]
