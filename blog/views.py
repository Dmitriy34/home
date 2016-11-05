from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404  ##см. "Расщиряем свое приложение"

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Как ты можешь заметить, мы создали метод (def) с именем post_list,
# который принимает в request в качестве аргумента
# и return (возвращает) результат работы метода render,
# который соберет наш шаблон страницы blog/post_list.html.


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})