# Generated by Django 3.1.7 on 2021-04-01 21:04

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(max_length=5000)),
                ('resume', ckeditor.fields.RichTextField(max_length=500)),
                ('image', models.ImageField(upload_to='static/home/assets/img/')),
                ('langage', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(blank=True, max_length=100)),
                ('writer_by', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, default='', upload_to=None)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(max_length=5000)),
                ('Resume', ckeditor.fields.RichTextField(max_length=250)),
                ('image', models.ImageField(upload_to=None)),
                ('langage', models.CharField(max_length=50)),
                ('Appellation', models.CharField(blank=True, max_length=100)),
                ('Zone', models.CharField(blank=True, max_length=100)),
                ('tag', models.CharField(blank=True, max_length=100)),
                ('writer_by', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, default='', upload_to=None)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PageBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(max_length=5000)),
                ('page_concept', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=None)),
                ('resume', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
