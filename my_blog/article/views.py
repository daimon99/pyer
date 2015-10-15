# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from django.http import Http404

from datetime import datetime


def home(request):
    # 获取全部的Article对象
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})
