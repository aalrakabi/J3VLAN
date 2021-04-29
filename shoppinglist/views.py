from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class ShoppinglistListView(ListView):
	model = Post
	template_name = 'home.html'

class ShoppinglistDetailView(DetailView): # new
	model = Post
	template_name = 'post_detail.html'
