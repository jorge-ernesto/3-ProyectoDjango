from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def list(request):

    # Sacar articulos
    # articles = Article.objects.all()
    articles = Article.objects.filter(public=1)
    
    # Paginar los articulos
    paginator = Paginator(articles, 2)
    
    # Recoger numero pagina
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': page_articles
    })

@login_required(login_url="login")
def category(request, category_id):

    # Obtenemos categoria
    category = Category.objects.get(id=category_id)
    # category = get_object_or_404(Category, id=category_id) # Devuelve error 404 si no esxiste el category_id

    # Obtenemos articulos
    # articles = Article.objects.filter(categories=category_id)
    # articles = Article.objects.filter(categories=category) # Tambien podemos pasarle el objeto completo
    # articles = category.article_set.all # Obtenemos articulos usando el objeto de categoria
    # articles = category.articles.all # Obtenemos articulos usando el objeto de categoria, gracias a la propiedad related_name="articles"
    articles = category.articles.filter(public=1)

    return render(request, 'categories/category.html', {
        'title': 'Categorias',
        'category': category,
        'articles': articles
    })

@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/article.html', {
        'article': article
    })
