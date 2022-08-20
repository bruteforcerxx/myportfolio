from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from .email import send_email  # requires parameters context, subject, destination, template
# from .models import UsersData, Contact
# from dash.models import Account
# Create your views here.


@api_view(['GET'])
def home_page(request):
    request.session.flush()
    page = 'index.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def about(request):
    request.session.flush()
    page = 'about.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def portfolio(request):
    request.session.flush()
    page = 'portfolio.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def contact(request):

    if request.method == 'GET':
        request.session.flush()
        page = 'contact.html'
        template = loader.get_template(page)
        context = {}
        return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)

    if request.method == 'POST':
        request.session.flush()
        page = 'contact.html'
        template = loader.get_template(page)
        context = {}
        return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def blog(request):
    request.session.flush()
    page = 'blog.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def blog_post(request):
    request.session.flush()
    page = 'blog_post.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)



