from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import TodoModel	 

class TodoList(ListView):
	template_name = "list.html"
	# 作成したデータをどのモデルに保存するのかを指定する
	model = TodoModel
	
class TodoDetail(DetailView):
	template_name = "detail.html"
	model = TodoModel
	
class TodoCreate(CreateView):
	template_name = "create.html"
	model = TodoModel
	fields = ("title", "memo", "priority", "duedate")
	# lazyつけるとデータが保存されてから実行する（らしい
	success_url = reverse_lazy("list")
	
class TodoDelete(DeleteView):
	template_name = "delete.html"
	model = TodoModel
	success_url = reverse_lazy("list")