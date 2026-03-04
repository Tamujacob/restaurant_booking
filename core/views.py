from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'login.html')   # ← just 'login.html', not 'admin/login.html'
