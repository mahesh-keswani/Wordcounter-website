from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
	return render(request, 'home.html')

def countwords(request):
	fulltext = request.GET['fulltext'].lower()
	fulltext_len = len(fulltext.split())
	fulltext_dict = dict(Counter(fulltext.split()))

	fulltext_dict = sorted(fulltext_dict.items(), key = lambda x: x[1], reverse = True)

	dict_to_pass = {'fulltext': fulltext, 'fulltext_len':fulltext_len, 'fulltext_dict':fulltext_dict}
	return render(request, 'count.html', dict_to_pass)

def about(request):
	return render(request, 'about.html')