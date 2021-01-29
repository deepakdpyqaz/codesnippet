from django.db import models

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.category

class Codes(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,unique=True)
    language=models.CharField(max_length=20,default='python')
    code=models.TextField()

    def __str__(self):
        return self.category.category +': '+self.title