from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from rest_framework import viewsets
from .serializers import NodeSerializer, NodeTreeSerializer
from .models import Node

class NodeView(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

def get_tree(request, root_id):
    try:
        root = Node.objects.get(pk=root_id)
    except:
        return HttpResponseNotFound("root not found")
    data = NodeTreeSerializer(root).data
    return JsonResponse({
        "status": "success",
        "result": data,
    })
