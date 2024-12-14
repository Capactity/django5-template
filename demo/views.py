import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def get_query(request):
    q = request.GET.get('q', 'default') # 获取查询字符串q的值，如果不存在则使用默认值'default'
    num = request.GET.get('num')
    # return HttpResponse("Query: %s, Num: %s" % (q, num))
    return JsonResponse({
        "code": 200,
        "msg": "success",
        "data": {
            "q": q,
            "num": num
        }
    })

# GET /path/<str:q>/<int:num>/
def get_path(request, q, num):
    return JsonResponse ({
        "code": 200,
        "msg": "success",
        "data": {
            "q": q,
            "num": num
        }
    })

@csrf_exempt
def post_formdate(request):
    q = request.POST.get('q', 'default')
    num = request.POST.get('num')
    return JsonResponse({
        "code": 200,
        "msg": "success",
        "data": {
            "q": q,
            "num": num
        }
    })

@csrf_exempt
def post_json(request):
    # 获取请求体中的JSON数据并解码为字符串
    data = request.body.decode('utf-8')
    # 解析json数据
    json_data = json.loads(data)
    q = json_data.get('q', 'default')
    num = json_data.get('num')
    return JsonResponse({
        "code": 200,
        "msg": "success",
        "data": {
            "q": q,
            "num": num
        }
    })