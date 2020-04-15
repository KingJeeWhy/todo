from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


# Create your views here.


def index(request):
    return render(request, "index.html")


class GetAll(APIView):
    def get(self, request):
        data = serializers.ArticleSerializer(models.Test.objects.all(), many=True).data
        res = {
            'success': True,
            'data': data
        }
        return Response(res)


class Delete(APIView):
    def get(self, request):
        id = request.GET['id']
        models.Test.objects.filter(id=id).delete()
        res = {
            'success': True,
        }
        return Response(res)


class Add(APIView):
    def get(self, request):
        name = request.GET['name']
        models.Test.objects.create(name=name,checked=0)
        res = {
            'success': True,
        }
        return Response(res)


class Change(APIView):
    def get(self, request):
        id = request.GET['id']
        checked = request.GET['checked']
        models.Test.objects.filter(id=id).update(checked=checked)
        res = {
            'success': True,
        }
        return Response(res)
