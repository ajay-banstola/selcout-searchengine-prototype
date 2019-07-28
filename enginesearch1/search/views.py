from django.shortcuts import render
from search.documents import MixtureDocument


# Create your views here.
def search(request):
	q = request.GET.get('q')
	
	if q:
		mixtures = MixtureDocument.search().query("match", name = q)
	else:
		mixtures = ''
		
	return render(request, 'search/search.html', {'mixtures':mixtures})
