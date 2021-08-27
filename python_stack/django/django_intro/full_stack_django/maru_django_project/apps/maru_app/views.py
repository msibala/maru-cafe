# from django.shortcuts import render

# # Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'maru_app/index.html')

def about(request):
    return render (request, 'maru_app/about.html')  

def notes(request):
    return render (request, 'maru_app/notes.html')  

def locations(request):
    return render (request, 'maru_app/locations.html')

def account(request):
    return render (request, 'maru_app/account.html')

def search(request):
    return render (request, 'maru_app/search.html')

def cart(request):
    return render (request, 'maru_app/cart.html')

def create_user(request):
    print("this is working")
    return render (request, 'maru_app/create_user.html')