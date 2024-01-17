from rest_framework import serializers

from .models import Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('name', 'parent')

class NodeTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, instance):
        children = []
        for child in instance.children:
            children.append(NodeTreeSerializer(child).data)
        children = sorted(children, key=lambda x: x['id'])
        return children
        

    class Meta:
        model = Node
        fields = ['id', 'name', 'parent', 'children']
