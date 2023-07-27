from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    #usando en default=timezone.now definimos de forma por defecto la hora actual de la publicacion de manera predeterminada
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=timezone.now)
    image = models.ImageField(verbose_name="Imagen", upload_to="Blog", null=True, blank=True)
    #en el autor identificamos una clave foranea donde la relacion es una una a muchos en la base de datos, esto quiere decir que un autor puede tener varios post pero los post no pueden tener varios autores, usando el on_detele definmos la forma de relacion encuanto a la eliminacion, tambien existe PROTECTED que hace que no se elimine el post, usando CASCADE al eliminar el autor se eliminaran sus post automaticamente
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # en las categorias tenemos una relacion de muchas a muchos donde los post puede tener varias categorias y las categorias pueden tener varios post de esta manera le deciamos a la base  de datos cuales son las relacion para hacer las consultas
    #usando en related_name podemos darle otro nombre a las categorias para luego preguntar por ellas 
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title