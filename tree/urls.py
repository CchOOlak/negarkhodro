from rest_framework import routers
from django.urls import path, include

from tree import views

router = routers.DefaultRouter()
router.register(r'nodes', views.NodeView, 'nodes')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tree/<int:root_id>/', views.get_tree),
]