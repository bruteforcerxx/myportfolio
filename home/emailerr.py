from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
import folium
from ipware import get_client_ip
import geocoder
from .models import VisitorData
from os.path import exists
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.


def report(context, request):
    ip, is_routable = get_client_ip(request)
    if ip is None:
        ips = geocoder.ip("me")
    else:
        if is_routable:
            ips = geocoder.ip(ip)
        else:
            ips = geocoder.ip("me")

    print(ips.city)
    print(ips.country)
    print(ips.latlng)
    mapper(ips.latlng)
    visitor = VisitorData(ip=ip)
    visitor.save()

    visitor = VisitorData.objects.filter(ip=ip)
    print(visitor)
    message = f"""You had a new visit to your website"""
    print(message)
    v_ip = f"Visitor's IP: {ip}"
    v_country = f"Visitor's Country: {ips.country}"
    v_city = f"Visitor's City: {ips.city}"
    v_fre = f"This IP has visited your website {len(visitor)} time(s)."

    context[0]['message'] = message
    context[0]['v_ip'] = v_ip
    context[0]['v_country'] = v_country
    context[0]['v_city'] = v_city
    context[0]['v_fre'] = v_fre
    context[0]['button_link'] = 'https://michaelolu.herokuapp.com/map_view'

    send_emailerr(context[0], context[1], context[2], context[3])


def mapper(location):
    print('generating map..')
    my_map3 = folium.Map(location=location, zoom_start=15)
    folium.Marker(location, popup=' Visitors location ').add_to(my_map3)

    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(dir, 'media')

    cwd = os.getcwd()
    dir = f"{path}\\map.html"
    print(dir)
    my_map3.save(dir)
    check = exists(dir)
    print('map generated.')
    print(f'###################map exists is {check}')


def send_emailerr(context, subject, destination, template):
    print('starting email sender....')
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    from_email = "My Portfolio <olumichael2015@outlook.com>"
    destination = str(destination)
    print('sending email....')
    status = mail.send_mail(subject, plain_message, from_email, [destination], html_message=html_message,
                            fail_silently=True)
    print(f'sender finished, status = {status}')
    return status

