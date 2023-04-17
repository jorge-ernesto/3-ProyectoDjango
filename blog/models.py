from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'  # Manipular nombre en el panel
        verbose_name_plural = 'Categorías'  # Manipular nombre en el panel

    def __str__(self):
        return self.name

class Article(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado')
    user = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE) # editable=False, no se puede editar. on_delete=models.CASCADE, significa que si borramos el usuario, borrara los articulos relacionados también
    categories = models.ManyToManyField(Category, verbose_name="Categorías", blank=True, related_name="articles") # null=True, para que el campo pueda ser NULL (Se quito ya que null=True no hace efecto en ManyToManyField). blank=True, no estaremos obligados a introducir ningun tipo de categoria. related_name="articles", nos permite acceder a los articulos desde el modelo categorias, buscar "category.articles"
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')

    class Meta:
        verbose_name = 'Artículo'  # Manipular nombre en el panel
        verbose_name_plural = 'Artículos'  # Manipular nombre en el panel
        ordering = ['-created_at']

    def __str__(self):
        return self.title
