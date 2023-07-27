from django.shortcuts import render, get_object_or_404
from .models import Post,Category
# Create your views here.
def blog(request):
    #obtenemos todos los post para luego iterarlos en el bucle for
    posts = Post.objects.all()
    # devuelve renderiza la url /template/blog/blog.html y pasa un disccionario para tener la variable dentro de la vista para usarla como variable{post.title} por ejemplo
    return render(request, "blog/blog.html", {'posts':posts})
def category(request, category_id):
    #controlamos el error por si al categoria no existe
    category = get_object_or_404(Category, id=category_id)
    #renderiza la vista /templates/blog/categories para mostrar las diferentes categorias, se añade un diccionario con las categorias para ser iterado y usado como variable en la vista categoria
    return render(request, "blog/category.html", {'category':category})
