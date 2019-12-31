from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
# Create your views here.


def home_page(request):
    username = request.session.get('username')
    return render(request, 'session/home.html', context={
        'username': username,
    })


class Login(View):

    def get(self, request):
        return render(request, 'session/login.html')

    def post(self, request):
        username = request.POST.get('username')
        request.session['username'] = username
        return redirect(reverse('home'))
