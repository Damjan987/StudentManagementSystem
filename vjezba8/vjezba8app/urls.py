from django.conf.urls import url
from vjezba8app import views

app_name = 'vjezba8app'

urlpatterns = [
    url(r'^predmetList/', views.PredmetListView.as_view(), name="predmetList"),
    url(r'^(?P<pk>\d+)/$', views.PredmetDetailView.as_view(), name="detail"),
    url(r'^createPredmet/$', views.PredmetCreateView.as_view(), name="create"),
    url(r'^updatePredmet/(?P<pk>\d+)/$', views.PredmetUpdateView.as_view(), name="update"),
    url(r'^korisnikList/', views.KorisnikListView.as_view(), name="list"),
    url(r'^student/(?P<pk>\d+)/$', views.KorisnikDetailView.as_view(), name="detail"),
]
