from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# def home(request):
# 	return render(request, )

class ShoppinglistListView(ListView):
	model = Post
	template_name = 'home.html'

class ShoppinglistDetailView(DetailView): 
	model = Post
	template_name = 'post_detail.html'

class ShoppinglistCreateView(CreateView): 
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'body']

class ShoppinglistUpdateView(UpdateView): 
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']

class ShoppinglistDeleteView(DeleteView): # new
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
