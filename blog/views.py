from django.shortcuts import render
from .models import Post # . - point mean current directory or current app
from django.utils import timezone

def page(request):
    pages = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/page.html', {'pages':pages})
