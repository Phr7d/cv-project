from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'cv/index.html')

def about(request):
    return render(request,'cv/about.html')

def resume(request):
    return render(request,'cv/resume.html')

def services(request):
    return render(request,'cv/services.html')

def portfolio(request):
    return render(request,'cv/portfolio.html')

def contact(request):
    return render(request,'cv/contact.html')

def portfoliodetails(request):
    return render(request,'cv/pd.html')


