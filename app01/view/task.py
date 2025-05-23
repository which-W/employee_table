from django.shortcuts import render, HttpResponse
from app01.models import Task
from app01.uels.bootstrap import Father_modelform
from django.views.decorators.csrf import csrf_exempt
import json
from app01.uels.pageform import Pagination


class Task_List(Father_modelform):
    class Meta:
        model = Task
        fields = {'name', 'description', 'level', 'user'}


def task_list(request):
    queryset = Task.objects.all().order_by("id")
    page_object = Pagination(request, queryset, page_size=4)
    form = Task_List()
    context = {
        'form': form,
        'queryset': page_object.queryset,
        'page_str': page_object.html()
    }
    return render(request, 'task_list.html', context)


@csrf_exempt
def task_add(request):
    form = Task_List(data=request.POST)
    if form.is_valid():
        form.save()
        data_list = {"status": True}
        return HttpResponse(json.dumps(data_list))
    else:
        data_list_2 = {"status": False, "message": "添加失败", 'error': form.errors}
        return HttpResponse(json.dumps(data_list_2, ensure_ascii=False))
