from django.template import loader
from django.http import HttpResponse

def reservations(request):
    template = loader.get_template('all_reservations.html')
    return HttpResponse(template.render())
# Create your views here.
