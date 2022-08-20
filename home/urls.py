from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('blog', views.blog, name='blog'),
    path('blog-post', views.blog_post, name='blog_post'),
]
