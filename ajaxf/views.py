from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def ajax_p(request):
    if request.is_ajax():
        name = request.POST.get('name', None)
        mail = request.POST.get('mail', None)
        passw = request.POST.get('password', None)
        
        if name and mail and passw:
            response = {'msg' : 'Account successfully created'}
            
            return JsonResponse(response)


# Create your views here.
