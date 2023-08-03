from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    department = models.CharField(max_length=20)
    age = models.IntegerField()





class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=50)
    description = models.TextField(default='Its too yummy')
    image = models.ImageField(upload_to='images')
    order_status = models.BooleanField(default=False)
    items = models.IntegerField(default=0)

    def __str__(self):
        return self.name