from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about.html')


def admissions(request):
    return render(request , 'admissions.html')

def student(request):
    return render(request , 'student.html')
