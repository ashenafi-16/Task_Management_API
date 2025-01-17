from django.shortcuts import render

def home(request):
    return render(request, 'task_manager/home.html')
