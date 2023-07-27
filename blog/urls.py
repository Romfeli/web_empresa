from django.urls import path
from . import views

urlpatterns = [
    #paths del blog
    path('', views.blog, name="blog"),
    #deficinos la ruta categorias y de forma dinamica el id, definicmos tambien que tipo de dato estamos recibiendo de esta manera tenemos int: para definirmo como in integer
    path('category/<int:category_id>/', views.category, name="category"),
]