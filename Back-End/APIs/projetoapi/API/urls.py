from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path(r'listar_criar', views.ListCreateUser.as_view()),
    path(r'atualizar_apagar/<int:pk>/', views.UpdateDestroyUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
