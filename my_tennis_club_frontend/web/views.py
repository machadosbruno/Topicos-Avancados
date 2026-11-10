from django.shortcuts import render, redirect
from .services import (
    get_members, get_member_by_id, get_plans,
    create_member, update_member, delete_member
)

def index_view(request):
    members = get_members()
    plans = get_plans()

    if request.method == 'POST':
        data = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'phone': request.POST.get('phone'),
            'joined_date': request.POST.get('joined_date') or None,
            'plan': request.POST.get('plan') or None,
        }

        files = None
        if 'foto' in request.FILES:
            files = {'foto': request.FILES['foto']}

        create_member(data, files)
        return redirect('index')
    
    return redirect(request, 'index.html', {'mymembers': members, 'myplans': plans})

def edit_member_view(request, member_id):
    member = get_member_by_id(member_id)
    plans = get_plans()

    if not member:
        return redirect('index')

    if request.method == 'POST':
        data = {
            'firstname': request.POST.get('firstname'),
            'lastname': request.POST.get('lastname'),
            'phone': request.POST.get('phone'),
            'joined_date': request.POST.get('joined_date') or None,
            'plan': request.POST.get('plan') or None,
        }

        files = None
        if 'foto' in request.FILES:
            files = {'foto': request.FILES['foto']}

        update_member(member_id, data, files)
        return redirect('index')

    context = {
        'member': member,
        'myplans': plans
    }
    return render(request, 'edit_member.html', context)

def delete_member_view(request, member_id):
    delete_member(member_id)
    return redirect('index')