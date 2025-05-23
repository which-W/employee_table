from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def depart_show(request):
    """部门展示"""

    depart_list = models.Department.objects.all()

    return render(request, 'depart_show.html', {'depart_list': depart_list})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    department = request.POST.get('department')
    models.Department.objects.create(title=department)
    return redirect('/depart/show')


def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()

    return redirect('/depart/show')


def depart_edit(request, nid):
    if request.method == 'GET':
        depart = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'depart': depart})
    department = request.POST.get('department')
    models.Department.objects.filter(id=nid).update(title=department)
    return redirect('/depart/show')
