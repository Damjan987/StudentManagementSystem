# Generated by Django 3.1.4 on 2021-01-13 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=255)),
                ('kod', models.CharField(max_length=16)),
                ('program', models.TextField()),
                ('bodovi', models.IntegerField()),
                ('sem_redovni', models.IntegerField()),
                ('sem_izvanredni', models.IntegerField()),
                ('izborni', models.CharField(choices=[('da', 'da'), ('ne', 'ne')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
                ('predmet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vjezba8app.predmet')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64)),
                ('role', models.CharField(choices=[('mentor', 'mentor'), ('student', 'student')], max_length=50)),
                ('status', models.CharField(choices=[('none', 'none'), ('redovni', 'redovni'), ('izvanredni', 'izvanredni')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
