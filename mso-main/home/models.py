from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Actus(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextField(max_length=5000)
	resume = RichTextField(max_length=500)
	image = models.ImageField(upload_to="static/home/assets/img/", height_field=None, width_field=None, max_length=100)
	langage = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	tag = models.CharField(max_length=100, blank=True)
	writer_by = models.CharField(max_length=100)
	video = models.FileField(upload_to=None, default='', blank=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class Article(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextField(max_length=5000)
	Resume = RichTextField(max_length=250)
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	langage = models.CharField(max_length=50)
	Appellation = models.CharField(max_length=100, blank=True)
	Zone = models.CharField(max_length=100, blank=True)
	tag = models.CharField(max_length=100, blank=True)
	writer_by = models.CharField(max_length=100)
	video = models.FileField(upload_to=None, default='', blank=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class PageBase(models.Model):
	title = models.CharField(max_length=100)
	body = RichTextUploadingField(max_length=5000)
	page_concept = models.BooleanField(default=False)
	image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	resume = models.TextField(max_length=1000, default="")

	def __str__(self):
		return self.title
