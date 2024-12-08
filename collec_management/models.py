from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Collec(models.Model):
    title=models.CharField(max_length=100,null=False)
    description=models.TextField(null=False)
    date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Ici, 1 est l'ID d'un utilisateur existant

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Utilisez un ID valide ici

    def __str__(self):
        return self.title
    

