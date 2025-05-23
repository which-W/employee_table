from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    return render(request, 'chart_list.html')


def chart_data(request):
    length = ['任务量']
    data_list = [
        {
            'name': '任务量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        }
    ]
    type_list = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']

    result = {
        'status': True,
        'data': {
            'length': length,
            'data_list': data_list,
            'type_list': type_list,
        }
    }
    return JsonResponse(result)
