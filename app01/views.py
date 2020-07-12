import json
from django.http import HttpResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt, csrf_protect #FBV模式下csrf中间件的控制
from django.utils.decorators import method_decorator #CBV模式下的csrf中间件控制


@csrf_exempt #表示当全站csrf中间件启用的时候，下面这个函数不使用csrf
@csrf_protect #表示当全站csrf中间件停用的时候，下面这个函数要使用csrf,这两种方式都属于FBV
def users(request):
    user_list = ['oldboy', 'alex']
    return HttpResponse(json.dumps(user_list))


class MyBaseView(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('after')
        return ret


class StudentView(MyBaseView, View):
    #
    # def dispatch(self, request, *args, **kwargs):
    #     # return HttpResponse("dispatch")
    #     func = getattr(self, request.method.lower())
    #     return func(request, *args, **kwargs)
    @method_decorator(csrf_exempt)#方式一：免除csrf的控制,必须加到dispatch函数下，加到post函数上不起作用
    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(StudentView, self).dispatch(request, *args, **kwargs)
        print('after')
        return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Delete")

@method_decorator(csrf_exempt,name='dispatch') #方式二：免除csrf的控制
class TeacherView(MyBaseView, View):
    # 没有自定义dispatch
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Delete")
