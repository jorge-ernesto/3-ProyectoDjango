from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    # Imprimimos en consola
    # print('PROCESSOR get_pages:', { 'pages': pages })

    return {
        'pages': pages
    }
