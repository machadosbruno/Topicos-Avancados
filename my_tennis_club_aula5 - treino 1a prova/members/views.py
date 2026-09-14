from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Member

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
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = Member(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('members'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = Member.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('members'))