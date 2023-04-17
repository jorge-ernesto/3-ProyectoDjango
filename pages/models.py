from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    title = models.CharField(max_length=50, verbose_name="Titulo")
    # content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigables")
    order= models.IntegerField(default="0", verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Pagina"  # Manipular nombre en el panel
        verbose_name_plural = "Paginas"  # Manipular nombre en el panel

    def __str__(self):
        return self.title
