from django.shortcuts import render

# Create your views here.
def login(request):
    request.session['page'] = "login"
    return render(request,'user/login.html')

def register(request):
    request.session['page'] = "register"
    return render(request,'user/register.html')