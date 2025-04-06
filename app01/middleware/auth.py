'''
Django的中间件非常方便 指的是信息从用户到浏览器和浏览器返回用户都要穿过三个process类
进入时候得通过process_request 返回时候 通过process_response
这就使得对没登陆用户的访问可以直接屏蔽 不需要在每个视图函数单独校验
应用中间件时候需要在settings中的MIDDLERWARE设置 按顺序执行
'''
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

# class M1(MiddlewareMixin):
#     """ 中间件1"""
#     def process_request(self,request):
#         # 如果此方法没有返回值(或返回None 仅有return的情况) 意味着可以继续往服务器走 如有直接从当前返回用户
#         print('m1 in')
#
#     def process_response(self,request,response):
#         print('m1 out')
#         return response

class AuthMiddleware(MiddlewareMixin):
    """ 用户登陆判断 没有登陆不可以访问 注意login页面需要排除 注意验证码也需排除 不然会死循环"""

    def process_request(self,request):
        if request.path_info == '/projectlogin/':
            return
        info_dict = request.session.get('info')
        if info_dict or request.path.startswith('/captcha/') or request.path.startswith('/projectlogin/add/'):
            return
        return redirect('/projectlogin/')
        # if request.session.get('info') or request.path_info == '/projectlogin/':
        #     return
        # return redirect('/projectlogin/')


    def process_response(self,request,response):

        return response