"""employee_table URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.view import depart, user, telephone, admin, account,task,order,chart

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/show', depart.depart_show),
    path('depart/add', depart.depart_add),
    path('depart/delete', depart.depart_delete),
    path('depart/<int:nid>/edit', depart.depart_edit),

    path('user/show', user.user_show),
    path('user/delete', user.user_delete),
    path('user/<int:nid>/edit', user.user_edit),
    path('user/add/info', user.user_add),
    path('user/<int:nid>/edits', user.user_edits),

    path('telephone/list', telephone.telephone_show),
    path('telephone/add', telephone.telephone_add),
    path('telephone/<int:nid>/edit', telephone.telephone_edit),
    path('telephone/<int:nid>/delete', telephone.telephone_delete),

    path('admin/list', admin.admin_list),
    path('admin/add', admin.admin_add),
    path('admin/<int:admin_id>/edit', admin.admin_edit),
    path('admin/<int:admin_id>/delete', admin.admin_delete),
    path('admin/<int:admin_id>/rest', admin.admin_rest),

    path('account/login', account.account_login),
    path('account/logout', account.account_logout),
    path('account/font', account.account_font, name='font'),

    path('task/list', task.task_list),
    path('task/add', task.task_add),

    path('order/list', order.order_list),
    path('order/add', order.order_add),
    path('order/delete', order.order_delete),
    path('order/detail', order.order_detail),
    path('order/edit', order.order_edit),

    path('chart/list', chart.chart_list),
    path('chart/data', chart.chart_data),

]
