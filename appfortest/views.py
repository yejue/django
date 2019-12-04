from django.shortcuts import render

# Create your views here.


def test_mode(request):
    return render(request, 'test/test_templates.html', context={
        'list1': [i for i in range(1, 10)],
    })


def index(request):
    return render(request, 'test/index.html')


def filter_content(request):
    return render(request, 'test/customize_fillter_test.html', context={
        'string': 'ABCDEFG'
    })
