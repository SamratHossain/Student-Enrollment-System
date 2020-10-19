from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField(max_length=200)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name