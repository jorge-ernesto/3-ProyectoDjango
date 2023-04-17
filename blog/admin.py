from django.contrib import admin
from .models import Category, Article

# Register your models here.

# Configuracion extra en el panel
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) # Debe tener una coma al final para que lo interprete como una tupla
    search_fields = ('name', 'description')
    list_display = ('name', 'created_at')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at') # Mostramos 'user', que es un campo de solo lectura
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')

    # Pequeño Hook
    # Funcionalidad para que agregue el usuario logueado
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
