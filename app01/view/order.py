from django.shortcuts import render
from django.http import JsonResponse
from app01.models import Order
# from app01.uels.bootstrap import Father_modelform
from django.views.decorators.csrf import csrf_exempt
from app01.uels.model_form import OrderModel
# from app01.models import Admin
from app01.uels.pageform import Pagination

def order_list(request):
    """
    This function is used to order the list of users
    """
    queryset = Order.objects.all().order_by("id")
    order = OrderModel()
    page_object = Pagination(request, queryset, page_size=10)
    context = {
        "form": order,
        'queryset': page_object.queryset,
        'page_str': page_object.html()
    }
    return render(request, "order_list.html", context)


@csrf_exempt
def order_add(request):
    """
    This function is used to add a new user
    """
    form = OrderModel(data=request.POST)
    if form.is_valid():
        form.instance.user_id = request.session['info']['id']
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    """
    This function is used to delete a user
    """
    uid = request.GET.get("uid")
    exits = Order.objects.filter(id=uid).exists()
    if exits:
        Order.objects.filter(id=uid).delete()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": "删除失败"})


@csrf_exempt
def order_detail(request):
    """
    This function is used to get the detail of a user
    """
    uid = request.GET.get("uid")
    row_dict = Order.objects.filter(id=uid).values('name', 'price', 'sale_situation').first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "没有数据"})
    result = {
        'status': True,
        'data': row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    uid = request.GET.get("uid")
    row_obj = Order.objects.filter(id=uid).first()
    if not row_obj:
        return JsonResponse({"status": False, "tips": "没有数据"})
    form = OrderModel(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})