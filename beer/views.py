from django.http import HttpResponse
from django.template import Context, loader
from beer.models import Beer

def index(request):
    beer_list = Beer.objects.all()
    template = loader.get_template('beer/index.html')
    c = Context({'beers':beer_list})
    return HttpResponse(template.render(c))
 
