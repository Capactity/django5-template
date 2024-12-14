from django.urls import path
# 从当前目录下导入views.py模块
from . import views

urlpatterns = [
    path('get_fbv/', views.get_query),
    path('get_fbv/<str:q>/<int:num>', views.get_path),
    path('post_fbv_formdate/', views.post_formdate),
    path('post_fbv_json/', views.post_json),
]