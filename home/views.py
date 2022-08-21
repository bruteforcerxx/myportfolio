from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view
from threading import Thread
from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from .emailerr import report  # requires parameters context, subject, destination, template
import folium
from folium import plugins
from .models import VisitorData
# from dash.models import Account
# Create your views here.


@api_view(['GET'])
def home_page(request):
    request.session.flush()

    #send mail
    name = 'Michael'
    message = 'You had a new visit to your website portfolio'
    button_link = ''
    button_text = 'View location on map'
    preheader_text = 'New website visit'
    buttom_message = 'This email is a report sent from your portfolio website.'
    context = {'name': name, 'message': message, 'button_link': button_link, 'button_text': button_text,
    'buttom_message': buttom_message, 'preheader_text': preheader_text}
    subject = 'portfolio visit'
    destination = 'olumichael2015@outlook.com'
    template = 'email.html'
    print('###########################sending mail.....#######################################')
    context = [context,  subject, destination, template]
    new_thrd = Thread(target=report, args=(context, request))
    new_thrd.start()
    # end send mail

    print('loading template....')
    page = 'index.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)


@api_view(['GET'])
def map_view(request):
    v = VisitorData.objects.all()
    location = eval(v[len(v) - 1].latlng)

    print(location)
    my_map3 = folium.Map(location=location, zoom_start=15)
    folium.Marker(location, popup="Last Visitor's location").add_to(my_map3)

    folium.plugins.Fullscreen().add_to(my_map3)

    page = 'map.html'
    m = my_map3._repr_html_()

    template = loader.get_template(page)
    context = {'map': m}
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
    page = 'my_map3.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)



