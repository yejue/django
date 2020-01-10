from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from little_blog.models import Blog
# Create your views here.


def index(request):
    username = request.user
    print(type(username))
    print(str(username))
    return render(request, 'auth_test/index.html', context={'username': str(username)})


class Login(View):

    def get(self, request):

        return render(request, 'auth_test/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.GET.get('next')

        user = authenticate(request, username=username, password=password)
        print(type(user))
        if user:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect(reverse('index'))


class Register(View):

    def get(self, request):
        return render(request, 'auth_test/resgiter.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        if password == password_repeat:
            User.objects.create_user(username=username, password=password)
            # User.objects.create_superuser(username=username, password=password)
            return redirect(reverse('login'))


@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'auth_test/blogs.html', context={'blogs': blogs})


@permission_required('Blog.delete_blog')
def delete(request, blog_id):
    Blog.objects.filter(id=blog_id).delete()
    return redirect('blog2')


# @method_decorator(login_required, name='get')
@method_decorator(permission_required('Blog.add_blog'), name='get')
class Write(View):

    def get(self, request):
        return render(request, 'auth_test/write.html')

    def post(self, request):
        blog_title = request.POST.get('article_title')
        blog_content = request.POST.get('article_content')

        Blog.objects.get_or_create(blog_title=blog_title, blog_content=blog_content)
        return redirect('write')


def login_out(request):
    logout(request)
    return redirect(reverse('index'))


def test1(request):
    user = User.objects.filter(username='yejue2')[0]
    print(user)
    print(type(user))
    perssion = Permission.objects.filter(codename='delete_blog')[0]
    user.user_permissions.add(perssion)
    return HttpResponse('添加成功')
