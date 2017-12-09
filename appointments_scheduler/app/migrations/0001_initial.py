# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_at', models.TimeField()),
                ('end_at', models.TimeField()),
            ],
            options={
                'verbose_name': 'Agendamento',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nome')),
                ('birthdate', models.DateField(max_length=3, verbose_name='Data de nascimento')),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, verbose_name='Sexo')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Paciente',
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Procedimento')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Procedimento',
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='app.Patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedure', to='app.Procedure'),
        ),
    ]
