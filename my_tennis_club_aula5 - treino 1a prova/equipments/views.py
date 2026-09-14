from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Equipment

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def equipments(request):
    myequipments = Equipment.objects.all().values()
    context = {
        'myequipments': myequipments
    }
    template = loader.get_template('all_equipments.html')
    return HttpResponse(template.render(context, request))

def add_equipments(request):
    template = loader.get_template('add_equipment.html')
    return HttpResponse(template.render({}, request))

def addrecord_equipment(request):
    x = request.POST['name']
    y = request.POST['number']
    z = request.POST['date']
    equipment = Equipment(name=x, register_number=y, register_date=z)
    equipment.save()
    return HttpResponseRedirect(reverse('equipments'))

def details_equipment(request, id):
    myequipment = Equipment.objects.get(id=id)
    template = loader.get_template('details_equipment.html')
    context = {
        'myequipment': myequipment
    }
    return HttpResponse(template.render(context, request))

def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    equipment.delete()
    return HttpResponseRedirect(reverse('equipments'))

def update_equipment(request, id):
    myequipment = Equipment.objects.get(id=id)
    template = loader.get_template('update_equipment.html')
    context = {
        'myequipment': myequipment,
    }
    return HttpResponse(template.render(context, request))

def updaterecord_equipment(request, id):
    name = request.POST['name']
    number = request.POST['number']
    date = request.POST['date']
    equipment = Equipment.objects.get(id=id)
    equipment.name = name
    equipment.register_number = number
    equipment.register_date = date
    equipment.save()
    return HttpResponseRedirect(reverse('equipments'))