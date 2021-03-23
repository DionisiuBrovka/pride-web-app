from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'test_pages/test_page.html')

def index(request):
    return render(request, 'index/index.html')

def error404(request, exception):
    return render(request, 'root/404.html')

def error500(request):
    return render(request, 'root/500.html')

def view_error404(request):
    return render(request, 'root/404.html')

def view_error500(request):
    return render(request, 'root/500.html')