from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def article_admin(request: HttpRequest):
    return render(request, 'admin_panel/articles/article_list.html')