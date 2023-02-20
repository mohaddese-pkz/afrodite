from django.shortcuts import render

def HomePage(request):
    return render(request, 'public_html/pages/index.html')