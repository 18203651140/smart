from django.http import HttpResponse
def index(request):
    return HttpResponse('hello world')
def about(request):
    return HttpResponse('123')
