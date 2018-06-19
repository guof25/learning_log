from django import forms         #form模块
from .models import Topic,Entry        #MODEL数据

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic             #根据哪个MODEL创建表单
        fields = ['text']          #表单中包含哪些字段
        labels = {'text':''}       #不为字段生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields =['text']
        #labels = {'text',''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}



