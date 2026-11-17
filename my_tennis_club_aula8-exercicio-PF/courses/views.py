from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Course
from instructors.models import Instructor
from django.db.models import Q
from django.core.paginator import Paginator

def courses(request):
    texto_busca = request.GET.get('busca', '')
    if texto_busca:
        mycourses = Course.objects.filter(
            Q(name__icontains=texto_busca) | Q(description__icontains=texto_busca)
        )
    else:
        mycourses = Course.objects.all()

    paginator = Paginator(mycourses, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        'texto_busca': texto_busca,
        'qtd': mycourses.count(),
    }
    template = loader.get_template('all_courses.html')
    return HttpResponse(template.render(context, request))

def detailscourse(request, id):
    mycourse = Course.objects.get(id=id)
    template = loader.get_template('detailscourse.html')
    context = {
        'mycourse': mycourse
    }
    return HttpResponse(template.render(context, request))

def addcourse(request):
    myinstructors = Instructor.objects.all().values()
    template = loader.get_template('addcourse.html')
    context = {
        'myinstructors':myinstructors,
    }
    return HttpResponse(template.render(context, request))

def addrecordcourse(request):
    x = request.POST['name']
    y = request.POST['description']
    z = Instructor.objects.filter(id=request.POST['instructor']).first()
    member = Course(name=x, description=y, instructor=z)
    member.save()
    return HttpResponseRedirect(reverse('courses'))

def deletecourse(request, id):
    member = Course.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('courses'))

def updatecourse(request, id):
    mycourse = Course.objects.get(id=id)
    myinstructor = Instructor.objects.all().values()
    template = loader.get_template('updatecourse.html')
    context = {
        'mycourse': mycourse,
        'myinstructor': myinstructor
    }
    return HttpResponse(template.render(context, request))

def updaterecordcourse(request, id):
    name = request.POST['name']
    description = request.POST['description']
    instructor = request.POST['instructor']
    member = Course.objects.get(id=id)
    member.name = name
    member.description = description
    member.instructor = Instructor.objects.get(id=instructor)
    member.save()
    return HttpResponseRedirect(reverse('courses'))
