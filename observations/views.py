from django.shortcuts import render
from django.http import HttpResponse


def test_func(request):
    # return HttpResponse('<h1> Welll dont know what to say to be more original</h1>')
    return render(request, 'test.html')