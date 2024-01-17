from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=250)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    @property
    def children(self):
        return Node.objects.filter(parent_id=self.id)

    def __str__(self) -> str:
        return self.name
