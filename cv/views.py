from django.shortcuts import render

def cv_view(request):
    context = {'name':'Amir', 'last_name':'Bornak'}
    return render(request, 'cv/index.html', context)