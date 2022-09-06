from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class HomePageFeed(ListView):
    model = Post
    template_name = "pages/post_list.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "object"

class PostCreateView(CreateView):
    model = Post
    template_name = "pages/post_new.html"
    fields = '__all__'
    success_url= reverse_lazy('pages/home.html')
    