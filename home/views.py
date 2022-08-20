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
from .emailerr import send_emailerr  # requires parameters context, subject, destination, template
# from .models import UsersData, Contact
# from dash.models import Account
# Create your views here.


@api_view(['GET'])
def home_page(request):
    request.session.flush()
    name = 'Michael'
    message = 'You had a new visit to your website portfolio'
    button_link = ''
    button_text = 'Visit site'
    preheader_text = 'New website visit'
    buttom_message = ''
    context = {'name': name, 'message': message, 'button_link': button_link, 'button_text': button_text,
    'buttom_message': buttom_message, 'preheader_text': preheader_text}
    subject = 'portfolio visit'
    destination = 'olumichael2015@outlook.com'
    template = 'email.html'
    print('###########################sending mail.....#######################################')
    print(send_emailerr(context, subject, destination, template))
    page = 'index.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def about(request):
    request.session.flush()
    page = 'about.html'
    template = loader.get_template(page)
    context = {'resume': 'media/resume.pdf'}
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


@api_view(['GET'])
def test(request):
    request.session.flush()
    page = 'email.html'
    template = loader.get_template(page)
    name = 'Michael'
    message = 'this is a test message'
    button_link = 'https://michaelolu.herokuapp.com'
    button_text = 'Visit site'
    buttom_message = 'This is a message'
    context = {'name': name, 'message': message, 'button_link': button_link, 'button_text': button_text,
    'buttom_message': buttom_message}

    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)



