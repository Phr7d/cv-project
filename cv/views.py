from django.shortcuts import render
# Create your views here.

context = {'name': 'Fred Shahin', 'birth':'17 July 1992', 'website':'https://www.phr7d.ir', 'Phone':'+98 912 408 8462', 'email':'m.aminshahin@gmail.com', 'Language':'Persian, English','Location':'No. 66, Molasadra, Vanak, Tehran, Iran'}
def home(request):
    return render(request,'cv/index.html')

def about(request):
    return render(request,'cv/about.html',context)

def resume(request):
    return render(request,'cv/resume.html')

def services(request):
    return render(request,'cv/services.html')

def portfolio(request):
    return render(request,'cv/portfolio.html')

def contact(request):
    return render(request,'cv/contact.html',context)

def portfoliodetails(request):
    return render(request,'cv/pd.html')


