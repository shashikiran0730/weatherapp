from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import requests
import json

def index(request):
    if request.method=='POST':
        city=request.POST['city']
        print(city)
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=497772d0b35ae08493a2f6ad5256011b"
        source=requests.get(url)
        print(source)
        if source!=None:
            data=json.loads(source.content)
            print("DATA",data)
            return render(request,"search.html",data)
        else:
            return render(request,"search.html")
    else:
       return render(request,"search.html")
    
def contact(request):
        if request.method=="POST":
            name=request.POST['email']
            content = request.POST['content']
            subject = "weatherapp"
            msg = content
            to = name
            res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
            if (res == 1):
                return render(request, "search.html")
            else:
                return HttpResponse("Mail could not sent")
        return render(request, "contact.html")

 
