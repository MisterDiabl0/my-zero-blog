from django.shortcuts import render
from django.http import HttpResponse

def page(request):
    return render(request, 'blog/page.html', {})

# def page(request):
#     return HttpResponse('ЗДРАВСТВУЙ, ПЛАНЕТА ЗЕМЛЯ')
