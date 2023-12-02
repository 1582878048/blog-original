from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from blogapp.models import UserInfo


def index(request):
     return HttpResponse("好好好！")


def insertDate(request):
     UserInfo.objects.create(name="mm", age=22, password="abc")
     return HttpResponse("Insert success!")


def queryAll(request):
     userList=UserInfo.objects.all()
     userNameList = ""
     for user in userList:
          print(user.id, user.name, user.age, user.password)
          userNameList = userNameList + "\n" + user.name
     return HttpResponse(userNameList)

def queryByld(request):
     userList=UserInfo.objects.filter(id=2)
     for user in userList:
          print(user.id,user.name,user.password)
     return HttpResponse("Query ok!!")

def updateById(request):
     UserInfo.objects.filter(id=2).update(password="123")
     return HttpResponse("Query ok!!!")

def deleteById(request):
     UserInfo.objects.filter(id=2).delete()
     return HttpResponse("Delete ok!!")


def queryData(request):
    res = dict()
    res["data"] = dict()
    res["code"] = 110
    res["msg"] = "请求成功"

    return HttpResponse(JsonResponse(res))
