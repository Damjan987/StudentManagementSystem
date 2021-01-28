"""vjezba8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import url, include
from vjezba8app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('admin/', admin.site.urls),
    url(r'^register/', views.register, name="register"),
    url(r'^user_login/$', views.user_login, name="user_login"),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^vjezba8app/', include('vjezba8app.urls', namespace='vjezba8app')),
    url(r'^upis_predmeta/(?P<predmet_id>\d+)/(?P<student_id>\d+)/$', views.upis_predmeta, name="upis_predmeta"),
    url(r'^brisanje_predmeta/(?P<predmet_id>\d+)/(?P<student_id>\d+)/$', views.brisanje_predmeta, name="brisanje_predmeta"),
    url(r'^polaganje_predmeta/(?P<predmet_id>\d+)/(?P<student_id>\d+)/$', views.polaganje_predmeta, name="polaganje_predmeta")
]
