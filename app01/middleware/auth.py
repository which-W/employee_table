from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class Auth_middleware(MiddlewareMixin):
    def process_request(self, request):
        # 如果请求路径为登录页面，则直接返回
        if request.path_info in ['/account/login', '/account/font']:
            return
        # 获取session中的用户信息
        info = request.session.get('info')
        # 如果没有用户信息，则重定向到登录页面
        if info:
            return
        return redirect('/account/login')

    def process_response(self, request, response):
        return response
