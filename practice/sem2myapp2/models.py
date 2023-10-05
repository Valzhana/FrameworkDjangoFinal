from django.db import models


# Create your models here.

class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField

    def fullname(self):
        return f'{self.f_name} {self.l_name}'

    def __str__(self):
        return f'{self.f_name}'
