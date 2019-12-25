from django.shortcuts import render, redirect
from .models import Blog
# Create your views here.


def index(request):
    return render(request, 'little_blog/index.html')


def blog_add(request):
    if request.method == 'GET':
        return render(request, 'little_blog/blog_add.html')
    elif request.method == 'POST':
        blog_title = request.POST.get('article_title')
        blog_content = request.POST.get('article_content')

        Blog.objects.get_or_create(blog_title=blog_title, blog_content=blog_content)

        return render(request, 'little_blog/blog_add.html', context={
            'msg': '添加成功',
        })


def blog_list(request):
    blog_lists = Blog.objects.all()
    return render(request, 'little_blog/blog_list.html', context={
        'blog_lists': blog_lists,
    })


def blog_detail(request, blog_id):
    blog_item = Blog.objects.filter(id=blog_id)
    return render(request, 'little_blog/blog_detail.html', context={
        'blog_item': blog_item[0],
    })


def delete(request, blog_id):
    Blog.objects.filter(id=blog_id).delete()
    return redirect('blog_list')


def edit(request, blog_id):
    if request.method == 'GET':
        blog_item = Blog.objects.filter(id=blog_id)
        return render(request, 'little_blog/blog_add.html', context={
            'edit': True,
            'blog_item': blog_item[0],
        })
    elif request.method == 'POST':
        blog_title = request.POST.get('article_title')
        blog_content = request.POST.get('article_content')

        Blog.objects.filter(id=blog_id).update(blog_title=blog_title, blog_content=blog_content)

        return redirect('blog_detail', blog_id=blog_id)


