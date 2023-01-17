from django.shortcuts import render
from polls.models import MyTable
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def unaut(request, post_id):
    if request.method == "POST":
        data = request.POST
        new = User.objects.create_user(username=data["log"],password=data["password"]) 
        new.save()
        
     
    
    return render(request,"index.html")
    
    



def usp(request, post_id):
    if request.method == "POST":
        data = request.POST
        
        user = authenticate(username=data["log"],password=data["password"])
        if  user == None:
            request.session["userid"] = False
            new = User.objects.create_user(data["log"],'example@example.com',data["password"])
            new.save()
            return render(request,"usp.html")
        else:
            request.session["auth"] = True
            request.session["person.id"]=True
            request.session["test"]="test"
            request.session["userid"] = True
            return render(request,"main.html")
            

            
    
    return render(request,"index.html")

def duxi(request):
   

    return HttpResponse(request,"duxi.html")



def picture(request):
    data = MyTable.objects.all()
    return render(request,"pic.html",{"data":data})













# Create your views here.
