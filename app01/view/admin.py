from django.shortcuts import render, redirect

from app01 import models
from app01.uels.pageform import Pagination
from app01.uels.model_form import Admin_form, Admin_change


def admin_list(request):
    info = request.session.get('info', '')
    if not info:
        return redirect('/account/login')
    admin_lists = {}
    value = request.GET.get('t', "")
    if value:
        admin_lists['username__contains'] = value
    admin_lists = models.Admin.objects.filter(**admin_lists)
    # Create a Pagination object to handle the pagination of the results
    page_object = Pagination(request, admin_lists, page_size=4)
    # Create a dictionary to store the results of the query
    context = {
        'admin_list': page_object.queryset,
        'page_str': page_object.html(),
        'search_data': value
    }

    # Return the rendered template with the results
    return render(request, 'admin_list.html', context)


def admin_add(request):
    if request.method == "GET":
        form = Admin_form()
        context = {
            'form': form
        }
        return render(request, 'admin_add.html', context)
    form = Admin_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')


def admin_edit(request, admin_id):
    admin = models.Admin.objects.filter(id=admin_id).first()
    if not admin:
        return redirect('/admin/list')
    form = Admin_form(instance=admin)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'admin_edit.html', context)
    form = Admin_form(instance=admin)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'admin_edit.html', {'form': form})


def admin_delete(request, admin_id):
    if request.method == "GET":
        admin = models.Admin.objects.get(id=admin_id)
        admin.delete()
        return redirect('/admin/list')


def admin_rest(request, admin_id):
    admin = models.Admin.objects.filter(id=admin_id).first()
    if not admin:
        return redirect('/admin/list')
    form = Admin_change(data=request.POST, instance=admin)
    return render(request, 'admin_rest.html', {'form': form})
