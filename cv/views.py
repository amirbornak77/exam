from django.shortcuts import render

def cv_view(request):
    context = {'name':'Amir', 'last_name':'Bornak', 'number': '(123)456-7890',
    'email': 'anyone@website.com', 'address' : '1600 Amphitheatre Parkway Mountain View, CA 94043 US'       }
    return render(request, 'cv/index.html', context)