from django.urls import path
from cv.views import *

app_name = 'cv'

urlpatterns = [
    path('',home,name='index'),
    path('about',about,name='about'),
    path('resume',resume,name='resume'),
    path('services',services,name='services'),
    path('portfolio',portfolio,name='portfolio'),
    path('contact',contact,name='contact'),
    path('pd',portfoliodetails,name='pd'),
] 