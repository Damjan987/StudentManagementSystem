from django.shortcuts import render, redirect
from vjezba8app.forms import UserForm, KorisnikInfoForm
from django.contrib.auth.hashers import make_password
from .models import Predmet, Korisnik, Upisi
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# CLASS BASED VIEWS START HERE

class PredmetListView(ListView):
    context_object_name = "predmeti"
    model = Predmet

class PredmetDetailView(DetailView):
    context_object_name = "predmet_detail"
    model = Predmet
    template_name = 'vjezba8app/predmet_detail.html'

class PredmetCreateView(CreateView):
    fields = ('ime', 'kod', 'program', 'bodovi', 'sem_redovni', 'sem_izvanredni', 'izborni')
    model = Predmet

class PredmetUpdateView(UpdateView):
    fields = ('ime', 'kod', 'program', 'bodovi', 'sem_redovni', 'sem_izvanredni', 'izborni')
    model = Predmet

class KorisnikListView(ListView):
    context_object_name = "korisnici"
    model = Korisnik

def filtriraj(k_id):
    svi_upisi = Upisi.objects.filter(student_id=k_id)
    return svi_upisi

class KorisnikDetailView(DetailView):
    context_object_name = "korisnik_detail"
    model = Korisnik
    template_name = 'vjezba8app/korisnik_detail.html'

    def get_context_data(self, **kwargs):
        context = super(KorisnikDetailView,self).get_context_data(**kwargs)
        context['predmeti'] = Predmet.objects.all()
        k_id = self.object.user.id
        #context['upisi'] = Upisi.objects.filter(student_id=self.object.user.korisnik.id)
        context['upisi'] = filtriraj(k_id)
        print("----------------- ", k_id, " -------------------")
        return context



# CLASS BASED VIEWS END HERE

# sa moodla pocinje tu

def upis_predmeta(request, predmet_id, student_id):
    predmet = Predmet.objects.get(id=predmet_id)
    korisnik = Korisnik.objects.get(id=student_id)
    taj_user = korisnik.user
    Upisi.objects.create(predmet_id=predmet, student_id=taj_user, status="rolled")
    return redirect("index")

def polaganje_predmeta(request, predmet_id, student_id):
    predmet = Predmet.objects.get(id=predmet_id)
    korisnik = Korisnik.objects.get(id=student_id)
    taj_user = korisnik.user
    taj_upis = Upisi.objects.filter(predmet_id=predmet, student_id=taj_user)
    taj_upis.delete()
    Upisi.objects.create(predmet_id=predmet, student_id=taj_user, status="passed")
    return redirect("index")

def brisanje_predmeta(request, predmet_id, student_id):
    predmet = Predmet.objects.get(id=predmet_id)
    korisnik = Korisnik.objects.get(id=student_id)
    taj_user = korisnik.user
    taj_upis = Upisi.objects.filter(predmet_id=predmet, student_id=taj_user, status="rolled")
    taj_upis.delete()
    return redirect("index")

#def upisni_list(request, student_id):
    #return redirect()

# sa moodla zavrsava tu

def index(request):
    return render(request, 'vjezba8app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = KorisnikInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = KorisnikInfoForm()
    return render(request, 'vjezba8app/registration.html',
                {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, "vjezba8app/login.html", {})
