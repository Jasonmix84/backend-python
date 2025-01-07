from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Safe'
    feature2.is_true = True
    feature2.details = 'Our service is very safe'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Affordable'
    feature3.is_true = False
    feature3.details = 'Our service is very affordable'

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features}) 

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})