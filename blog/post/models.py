
#importamos las librerias necesarias
from django.db import models
from django.utils import timezone

#definimos nuestro modelo como una clase de Python normal y corriente
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


#definimos que campos se pueden filtrar en el administrador de django
    def publish(self):
        self.published_date = timezone.now()
        self.save()

#definimos los campos principales de nuestro modelo
    def __str__(self):
        return self.title
