from django.db import models

# Create your models here.

class Collec(models.Model):
    title=models.CharField(max_length=100,null=False)
    description=models.TextField(null=False)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Element(models.Model):
    title=models.CharField(max_length=50,null=False)
    description=models.TextField(null=False)
    value=models.IntegerField(null=False)
    quantity=models.IntegerField(null=False)
    date=models.DateField(null=False)
    collection=models.ForeignKey(
        Collec, on_delete=models.CASCADE
    )