from django.http import HttpResponse
from django.template import loader
from .models import Member
#Teste da página de erro de permissão negada (403.html)
from django.core.exceptions import PermissionDenied

def members(request):
    mymembers = Member.objects.all().values()
    context = {
        'mymembers': mymembers
    }
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    #Teste da página de erro de permissão negada (403.html)
    #raise PermissionDenied("Erro")
    template = loader.get_template('main.html')
    return HttpResponse(template.render())