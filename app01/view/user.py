from django.shortcuts import render, redirect
from app01 import models
from app01.uels.pageform import Pagination
from app01.uels.model_form import Userinfo_form


# Create your views here.


def user_show(request):
    info = request.session.get('info', '')
    if not info:
        return redirect('/account/login')
    user_list = {}
    value = request.GET.get('p', "")
    if value:
        user_list['mobile__contains'] = value
    user_list = models.Employee_Table.objects.filter(**user_list)

    page_object = Pagination(request, user_list, page_size=3)
    context = {
        'user_list': page_object.queryset,
        'page_str': page_object.html()
    }

    return render(request, 'user_list.html', context)


def user_delete(request):
    nid = request.GET.get('nid')
    models.Employee_Table.objects.filter(id=nid).delete()

    return redirect('/user/show')


def user_edit(request, nid):
    if request.method == 'GET':
        user = models.Employee_Table.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'user': user})
    username = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    salary = request.POST.get('salary')
    date = request.POST.get('date')
    depart_id = request.POST.get('department')
    models.Employee_Table.objects.filter(id=nid).update(name=username,
                                                        age=age,
                                                        gender=gender,
                                                        salary=salary,
                                                        date=date,
                                                        depart_id=depart_id)
    return redirect('/user/show')


def user_add(request):
    if request.method == 'GET':
        form = Userinfo_form()
        return render(request, 'user_add.html', {'form': form})
    form = Userinfo_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/show')
    return render(request, 'user_add.html', {'form': form})


def user_edits(request, nid):
    row = models.Employee_Table.objects.filter(id=nid).first()
    form = Userinfo_form(instance=row)
    if request.method == 'GET':
        return render(request, 'user_edits.html', {'form': form})
    form = Userinfo_form(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/user/show')
    return render(request, 'user_edits.html', {'form': form})


