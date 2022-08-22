from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
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

    visitor = VisitorData.objects.filter(ip=ip)
    x = float(len(visitor))
    ltg = str(ips.latlng)
    visitor = VisitorData(ip=ip, latlng=ltg, sn=x)
    visitor.save()
    visitor = VisitorData.objects.filter(ip=ip)
    print(visitor)
    all_visit = VisitorData.objects.all()
    message = f"""You had a new visit to your website"""
    print(message)
    v_ip = f"Visitor's IP: {ip}"
    v_country = f"Visitor's Country: {ips.country}"
    v_city = f"Visitor's City: {ips.city}"
    v_fre = f"This IP has visited your website {len(visitor)} time(s)."
    v_total = f"You have a total of {len(all_visit)} visits to your portfolio"

    context[0]['message'] = message
    context[0]['v_ip'] = v_ip
    context[0]['v_country'] = v_country
    context[0]['v_city'] = v_city
    context[0]['v_fre'] = v_fre
    context[0]['v_total'] = v_total
    context[0]['button_link'] = 'https://michaelolu.herokuapp.com/map_view'

    send_emailerr(context[0], context[1], context[2], context[3])


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

