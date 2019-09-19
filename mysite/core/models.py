from django.db import models

class Book(models.Model):
    clase = models.PositiveIntegerField()
    tema = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='books/pdf/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.archivo.delete()
        super().delete(*args, **kwargs) 



