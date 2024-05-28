from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    articcles=Article.objects.order_by('-date')
    return render(request,'index.html', {'articcles': articcles})

def article(request):
    article=Article.objects.order_by('-category')
    return render(request,'article.html', {'article': article})

def category(request):
    article_list=Article.objects.order_by('-category')
    return render(request, 'category.html', {'article_list': article_list})

def allnews(request):
    all_articles=Article.objects.order_by('-date')
    return render(request, 'allnews.html', {'all_articles': all_articles})

def about(request):
    return render(request, 'about.html')

def rule(request):
    return render(request, 'rule.html')

def price(request):
    return render(request, 'price.html')

def confidentiality(request):
    return render(request, 'Confidentiality.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

