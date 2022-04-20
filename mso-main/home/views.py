from django.http import HttpResponse
from django.shortcuts import render

from .models import Actus, Article, PageBase


def index(request):
	page_concept_resume = PageBase.objects.order_by('title')
	latest_actuality_one = Actus.objects.order_by('-created_at')[0]
	latest_actuality_two = Actus.objects.order_by('-created_at')[1]
	latest_actuality_three = Actus.objects.order_by('-created_at')[2]

	context = {
		'latest_actuality_one': latest_actuality_one,
		'latest_actuality_two': latest_actuality_two,
		'latest_actuality_three': latest_actuality_three,
		'page_concept_resume': page_concept_resume,
	}
	return render(request, 'home/index.html', context)

def concept(request):
	message = "Page Concept"
	return HttpResponse(message)


def actus(request):
	actualities = Actus.objects.order_by('-created_at')
	formatted_actus = ["<li>{}</li>".format(actu.title) for actu in actualities]
	message = """<ul>{}</ul>""".format("\n".join(formatted_actus))
	return HttpResponse(message)

def contact(request):
	message = "Formulaire de contact"
	return HttpResponse(message)


def produits(request):
	products = Article.objects.order_by('-created_at')
	formatted_product = ["<li>{}</li>".format(prod.title) for prod in products]
	message = """<ul>{}</ul>""".format("\n".join(formatted_product))
	return HttpResponse(message)


def detailActu(request, actu_id):
	id = int(actu_id)
	actu = Actus.id
	message = "le titre de l'actu est {} et le corps {}".format(actu['title'], actu['body'])
	return HttpResponse(message)


def detailProduit(request):
	message = "detail de l'article produit"
	return HttpResponse(message)