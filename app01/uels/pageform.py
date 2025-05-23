"""
自定义分页组件
"""
"""
    使用时需要自我调动queryset获取每页的数据量
    比如这样写（page_size为前后页数）
     user_list = models.Employee_Table.objects.all() 或者改成f的选择
    page_object = Pagination(request, user_list, page_size=3)
    以字典的形式传入render中
    context = {
        'user_list': page_object.queryset,
        'page_str': page_object.html()
    }
    
"""
"""
    在html中的要求
    {% for user in user_list %}
    {{ user.xxx}}
    {% endfor %}
    显示分页
     <ul class="pagination">
                {{ page_str }}
    </ul>
"""
from django.utils.safestring import mark_safe
import copy


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=2):
        """

        :param request: 获取请求对象
        :param queryset: 符合条件的数据（根据这个数据进行处理）
        :param page_size:每页显示多少条数据
        :param page_param:在url中获取的页码参数
        :param plus:当前页的前后页的个数
        """
        page = request.GET.get(page_param, '1')
        query_dic = copy.deepcopy(request.GET)
        query_dic._mutable = True
        self.query_dic = query_dic
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.queryset = queryset[self.start: self.end]
        telephone_number = queryset.count()
        page_all, div = divmod(telephone_number, page_size)
        if div:
            page_all += 1
        self.page_all = page_all
        self.plus = plus
        self.page_param = page_param

    def html(self):
        if self.page_all <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.page_all
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.page_all:
                    end_page = self.page_all
                    start_page = self.page_all - 2 * self.plus
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        page_list = []
        self.query_dic.setlist(self.page_param, [1])
        pre = "<li><a href='?{}'>首页</a></li>".format(self.query_dic.urlencode())
        page_list.append(pre)

        if self.page > 1:
            self.query_dic.setlist(self.page_param, [self.page - 1])
            pre = "<li><a href='?{}'>上一页</a></li>".format(self.query_dic.urlencode())
        else:
            self.query_dic.setlist(self.page_param, [1])
            pre = "<li><a href='?{}'>上一页</a></li>".format(self.query_dic.urlencode())
        page_list.append(pre)
        for i in range(start_page, end_page + 1):
            self.query_dic.setlist(self.page_param, [i])
            if i == self.page:
                element = "<li class='active'><a  href='?{}'>{}</a></li>".format(self.query_dic.urlencode(), i)
            else:
                element = "<li><a href='?{}'>{}</a></li>".format(self.query_dic.urlencode(), i)
            page_list.append(element)
        if self.page < self.page_all:
            self.query_dic.setlist(self.page_param, [self.page + 1])
            pre = "<li><a href='?{}'>下一页</a></li>".format(self.query_dic.urlencode())
        else:
            self.query_dic.setlist(self.page_param, [self.page_all])
            pre = "<li><a href='?{}'>下一页</a></li>".format(self.query_dic.urlencode())
        page_list.append(pre)
        self.query_dic.setlist(self.page_param, [self.page_all])
        ends = "<li><a href='?{}'>尾页</a></li>".format(self.query_dic.urlencode())
        page_list.append(ends)
        page_list_str = mark_safe("".join(page_list))
        return page_list_str
