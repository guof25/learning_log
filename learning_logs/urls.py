from django.urls import path
from . import views

urlpatterns = [
    #主页
    path('',views.index,name = 'index'),
    #显示TOPIC主题相关部分
    path('topics/',views.topics,name = "topics"),
    #显示topic特定主题
    path('topics/<int:topic_id>/',views.topic,name = 'topic'),
    #用于添加新主题的网页
    path('new_topic/',views.new_topic,name = 'new_topic'),
    #用于添加新ENTRY的网页
    path('new_entry/<int:topic_id>/',views.new_entry,name = 'new_entry'),
    #编辑ENTRY
    path('edit_entry/<int:entry_id>',views.edit_entry,name = "edit_entry"),
]