from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.urls import reverse
from django.shortcuts import render

class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=64)
    ROLE_ENUM = (('mentor', 'mentor'), ('student', 'student'))
    role = models.CharField(max_length=50, choices=ROLE_ENUM)
    STATUS_ENUM = (('none', 'none'), ('redovni', 'redovni'), ('izvanredni', 'izvanredni'))
    status = models.CharField(max_length=50, choices=STATUS_ENUM)
    def __str__(self):
        return self.email

class Predmet(models.Model):
    ime = models.CharField(max_length=255)
    kod = models.CharField(max_length=16)
    program = models.TextField()
    bodovi = models.IntegerField()
    sem_redovni = models.IntegerField()
    sem_izvanredni = models.IntegerField()
    IZBORNI_ENUM = (('da', 'da'), ('ne', 'ne'))
    izborni = models.CharField(max_length=50, choices=IZBORNI_ENUM)
    def __str__(self):
        return self.ime

    def get_absolute_url(self):
        return reverse("vjezba8app:detail", kwargs={'pk':self.pk})


class Upisi(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE)
    predmet_id = models.ForeignKey(Predmet, on_delete=models.CASCADE)
    status = models.CharField(max_length=64)
    def __str__(self):
        return self.status
