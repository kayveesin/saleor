
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^', views.myview, name='donation-input'),
    url(r'^donationpdf', views.myview, name='donation-pdf'),

]
