# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    post_list = Article.objects.all() #获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

from django.http import Http404
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})

from datetime import datetime
def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
