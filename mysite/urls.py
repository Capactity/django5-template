"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

# 欢迎信息

def welcome(request):
    return HttpResponse("Welcome to Django5")

# 路由配置
urlpatterns = [
    # path 函数用于定义路由，第一个参数是路径，第二个参数是处理请求的视图函数。name参数是给路由起一个名字，方便在模板中使用。
    path('admin/', admin.site.urls),
    path('', welcome, name='welcome'),
    path('demo/', include('demo.urls')), # 加载demo应用的路由
]
