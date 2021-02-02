from django.shortcuts import render
from django.views import View
from .models import User

from django.http import JsonResponse

from django.forms.models import model_to_dict
# Create your views here.


class UserListView(View):
    def get(self, request):
        uList = User.objects.all()
        return JsonResponse(list(uList.values()), safe = False)

    # def post(self, request):
        # post..

    # def put(self, request):
    #     # put..

    # def delete(self, request):
    #     # delete..

class UserDetailtView(View):
    def get(self, request, pk):
        userDetail = User.objects.get(pk=pk)
        print(JsonResponse(model_to_dict(userDetail), safe = False))
        return JsonResponse(model_to_dict(userDetail), safe = False)
    # def post(self, request):
    #     # post..
    # def put(self, request):
    #     # put..
    # def delete(self, request):
    #     # delete..