from django.shortcuts import render
# Create your views here.


def send_msg(request):
    return render(request,'login.html',{'name':'Json'})