from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Instructor
from django.db.models import Q
from django.core.paginator import Paginator

def instructors(request):
    texto_busca = request.GET.get('busca', '')
    if texto_busca:
        myinstructors = Instructor.objects.filter(
            Q(name__icontains=texto_busca)
        )
    else:
        myinstructors = Instructor.objects.all()

    paginator = Paginator(myinstructors, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'texto_busca': texto_busca,
        'qtd': myinstructors.count(),
    }
    template = loader.get_template('all_instructors.html')
    return HttpResponse(template.render(context, request))

def detailsinstructor(request, id):
    myinstructor = Instructor.objects.get(id=id)
    template = loader.get_template('detailsinstructor.html')
    context = {
        'myinstructor': myinstructor
    }
    return HttpResponse(template.render(context, request))

def addinstructor(request):
    myinstructor = Instructor.objects.all().values()
    context = {
        'myinstructor': myinstructor
    }
    template = loader.get_template('addinstructor.html')
    return HttpResponse(template.render(context, request))

def addrecordinstructor(request):
    x = request.POST['nome']
    foto = None
    if 'foto' in request.FILES:
        foto = request.FILES['foto']
    instructor = Instructor(name=x, photo=foto)
    instructor.save()
    return HttpResponseRedirect(reverse('instructors'))

def deleteinstructor(request, id):
    instructor = Instructor.objects.get(id=id)
    instructor.delete()
    return HttpResponseRedirect(reverse('instructors'))

def updateinstructor(request, id):
    myinstructor = Instructor.objects.get(id=id)
    template = loader.get_template('updateinstructor.html')
    context = {
        'myinstructor': myinstructor
    }
    return HttpResponse(template.render(context, request))

def updaterecordinstructor(request, id):
    name = request.POST['nome']
    instructor = Instructor.objects.get(id=id)
    instructor.name = name
    if 'foto' in request.FILES:
        foto = request.FILES['foto']
        instructor.foto = foto
    instructor.save()
    return HttpResponseRedirect(reverse('instructors'))
