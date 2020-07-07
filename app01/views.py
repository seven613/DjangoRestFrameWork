import json
from django.http import HttpResponse
from django.views import View


def users(request):
    user_list = ['oldboy', 'alex']
    return HttpResponse(json.dumps(user_list))


class StudentView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT")

    def delete(self, request, *args, **kwargs):
        return HttpResponse("Delete")