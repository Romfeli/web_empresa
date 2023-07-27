from django.contrib import admin
from .models import Category, Post
# Register your models here.
    ##definimos la visualizacion del administrados DJANGO en las categorias

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    ##definimos la visualizacion del administrados DJANGO en los post
class PostAdmin(admin.ModelAdmin):
    # esta funciona define solo lectura para los campos del administrados
    readonly_fields = ('created','updated')
    #esta funcion muestra los campos que querramos en el administrador
    #podemos crear campos manuales definiendolos como funciones mas abajo tenemos el ejemplo de como hacerlo
    list_display = ('title', 'author', 'published','post_categories')
    #esta funcion ordena de la forma que eligamos, primero por el autor y luego por fecha de publicacion
    ordering = ('author', 'published')
    #esta funcion nos muestra una barra de busqueda, donde podemos proporsionar todos los datos disponibles para la busqueda, por titulo, por contenido, 
    #en caso de los autores donde el nombre es difrente en la base de datos tenemos que informarlo con ___ como el author que en la base de datos esta como username y en las categorias usamos en name para referise ccada uno de las categorias
    search_fields = ('title','content','author__username', 'categories__name')
    #esta funcion nos da un menu en la aprte superior donde podemos filtar por hecha de publicacion la lista de post
    date_hierarchy = 'published'
    #esta funcion nos muestra en la seccion derecha los autores o categorias para poder filtrar de la forma que querramos
    list_filter = ('author__username','categories__name')
    #en este funcion definimos un campo manuelmente para luego se utilizado en  list_display de forma que usamos el nombre de la funcion como nombre del campo y luego realizamos una iteracion para optener todas las categorias e insertarlas divididas por una coma  y usando un .join de forma que usando un bucle for iteramos todas las catergorias y las ordenamos por nombre
    # 
    def post_categories(self, obj):

        return ", ".join(c.name for c in obj.categories.all().order_by("name"))
    #este variable la utilizamos para cambiarle el nombre de forma manual a la funcion y que sea mas personalizable
    post_categories.short_description = "Categorias"


#registramos el uso de la Caterogias en el panel de administracion
admin.site.register(Category, CategoryAdmin)
#registramos el uso de la post en el panel de administracion

admin.site.register(Post, PostAdmin)