from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
# Create your views here.


def send_emailerr(context, subject, destination, template):
    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)
    from_email = "My Portfolio <olumichael2015@outlook.com>"
    destination = str(destination)
    status = mail.send_mail(subject, plain_message, from_email, [destination], html_message=html_message,
                            fail_silently=True)
    return status
