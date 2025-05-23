from django.shortcuts import render, redirect
from app01 import models
from app01.uels.pageform import Pagination
from app01.uels.model_form import Telephone_form


# Create your views here.


def telephone_show(request):
    info = request.session.get('info', '')
    if not info:
        return redirect('/account/login')
    telephone_list = {}
    value = request.GET.get('q', "")
    if value:
        telephone_list['mobile__contains'] = value

    queryset = models.Telephone_User.objects.filter(**telephone_list).order_by('-level')
    pagination = Pagination(request, queryset)
    # page = int(request.GET.get('page', 1))
    # page_size = 10
    # start = (page - 1) * 10
    # end = page * 10
    queryset = pagination.queryset
    page_list_str = pagination.html()

    # telephone_number = models.Telephone_User.objects.filter(**telephone_list).count()
    # page_all, div = divmod(telephone_number, pagination.page_size)
    # plus = 2
    # if page_all <= 2 * plus + 1:
    #     start_page = 1
    #     end_page = page_all
    # else:
    #     if page <= plus:
    #         start_page = 1
    #         end_page = 2 * plus + 1
    #     else:
    #         if (page + plus) > page_all:
    #             end_page = page_all
    #             start_page = page_all - 2 * plus
    #         else:
    #             start_page = page - plus
    #             end_page = page + plus
    #
    # page_list = []
    # pre = "<li><a href='?page={}'>首页</a></li>".format(1)
    # page_list.append(pre)
    #
    # if page > 1:
    #     pre = "<li><a href='?page={}'>上一页</a></li>".format(page - 1)
    # else:
    #     pre = "<li><a href='?page={}'>上一页</a></li>".format(1)
    # page_list.append(pre)
    # for i in range(start_page, end_page + 1):
    #     if i == page:
    #         element = "<li class='active'><a  href='?page={}'>{}</a></li>".format(i, i)
    #     else:
    #         element = "<li><a href='?page={}'>{}</a></li>".format(i, i)
    #     page_list.append(element)
    # if page < page_all:
    #     pre = "<li><a href='?page={}'>下一页</a></li>".format(page + 1)
    # else:
    #     pre = "<li><a href='?page={}'>下一页</a></li>".format(page_all)
    # page_list.append(pre)
    # ends = "<li><a href='?page={}'>尾页</a></li>".format(page_all)
    # page_list.append(ends)
    # page_list_str = mark_safe("".join(page_list))
    context = {'forms': queryset,
               'page_str': page_list_str}
    return render(request, 'telephone.html', context)


# fields = '__all__'也可以

# def single_mobile(self):
#     text_phone = self.cleaned_data['mobile']
#
#     exits = models.Telephone_User.objects.filter(mobile=text_phone).exists()
#       检验除自己以外的是否重复用在编辑按钮之中
#       exits = models.Telephone_User.object.exclude(id = self.instance.pk).filter(mobile=text_phone).exists()
#     if exits:
#         raise ValueError('号码重复')
#
#     return text_phone


def telephone_add(request):
    if request.method == 'GET':
        form = Telephone_form()
        return render(request, 'Telephone_add.html', {'form': form})
    form = Telephone_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/telephone/list')
    return render(request, 'Telephone_add.html', {'form': form})


def telephone_edit(request, nid):
    row = models.Telephone_User.objects.filter(id=nid).first()
    form = Telephone_form(instance=row)
    if request.method == 'GET':
        return render(request, 'telephone_edit.html', {'form': form})
    form = Telephone_form(data=request.POST, instance=row)
    if form.is_valid():
        form.save()
        return redirect('/telephone/list')
    return render(request, 'telephone_edit.html', {'form': form})


def telephone_delete(request, nid):
    models.Telephone_User.objects.filter(id=nid).delete()
    return redirect('/telephone/list')
