from blog.models import Category, Article

def get_categories(request):

    # No flat=True, devuelve <QuerySet [(2,), (1,), (2,)]>
    # categories_in_use = Article.objects.filter(public=True).order_by('id').values_list('categories')

    # flat=True, devuelve <QuerySet [2, 1, 2]>, no es válido cuando se llama a values_list con más de un campo
    categories_in_use = Article.objects.filter(public=True).order_by('id').values_list('categories', flat=True)

    # filter(id__in=ids), es una subconsulta
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name', 'description')

    # Imprimimos en consola
    # print('PROCESSOR get_categories:', { 'categories': categories, 'ids': categories_in_use })

    return {
        'categories': categories,
        'ids': categories_in_use
    }
