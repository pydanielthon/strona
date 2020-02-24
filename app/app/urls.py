"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import homepage, address, orders, recovery, payment, profile, singin, ticket, tickets, wishlist, complete, details, payments, review, shipping, contacts, add, sales, otracking, scart, categories, grid 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^address/$', address, name='address'),
    url(r'^orders/$', orders, name='orders'),
    url(r'^recovery/$', recovery, name='recovery'),
    url(r'^payment/$', payment, name='payment'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^singin/$', singin, name='singin'),
    url(r'^ticket/$', ticket, name='ticket'),
    url(r'^tickets/$', tickets, name='tickets'),
    url(r'^wishlist/$', wishlist, name='wishlist'),
    url(r'^complete/$', complete, name='complete'),
    url(r'^details/$', details, name='details'),
    url(r'^payments/$', payments, name='payments'),
    url(r'^review/$', review, name='review'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^add/$', add, name='add'),
    url(r'^sales/$', sales, name='sales'),
    url(r'^otracking/$', otracking, name='otracking'),
    url(r'^scart/$', scart, name='scart'),


    url(r'^shipping/$', shipping, name='shipping'),
    url(r'^categories/$', categories, name='categories'),
    url(r'^grid/$', grid, name='grid'),
]
