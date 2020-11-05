from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Profile,C,Cpp,Java,Python,ConnectRequest
import random 
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        n=request.user
        print(f"{n} at home")
        i=Profile.objects.filter(username=n).first().intrest
        m=Profile.objects.filter(username=n).first().marks
        print(i,m)
        if i=='' or m==0:
            print("whyyyyyyy")
            return redirect("timeline")
        else:
            return redirect("profile")
    else:
        return render(request,"base.html")

def timeline(request):
    n=request.user
    i=Profile.objects.filter(username=n).first().intrest
    print(i)
    m=Profile.objects.filter(username=n).first().marks
    if i =='':
        print("aaaaaaaaaaaa")
        if request.method=="POST":
            choice=request.POST['choice']
            print(choice)
            Profile.objects.filter(username=n).update(intrest=choice) 
            return redirect("test")
        return render(request,"code/choice.html")
    if m==0:
        return redirect("test")
    return render(request,"base.html")

def test(request):
    n=request.user
    if Profile.objects.filter(username=n).first().marks == 0:
        choice=Profile.objects.filter(username=n).first().intrest
        if choice=='C++':
            que=Cpp.objects.all()
        if choice=='C':
            que=C.objects.all()
        if choice=='Java':
            que=Java.objects.all()
        if choice=='Python':
            que=Python.objects.all()
        print(choice)
        quesitions=[]
        un=['a','b','c','d','e','f','g','h','i','j']
        #un=['a','b','c']
        for q in que:
            if q not in quesitions:
                quesitions.append(q)
            else:
                continue
        sampling = random.sample(quesitions, 10)
   
        d = dict(zip(un,sampling))
        answers=[]
        if request.method=="POST":
            answers.append(request.POST['a'])
            answers.append(request.POST['b'])
            answers.append(request.POST['c'])
            answers.append(request.POST['d'])
            answers.append(request.POST['e'])
            answers.append(request.POST['f'])
            answers.append(request.POST['g'])
            answers.append(request.POST['h'])
            answers.append(request.POST['i'])
            answers.append(request.POST['j'])      
            correctAnswers=[]
            marks=0
            for q in sampling:
                correctAnswers.append(q.ans)
            for i in range(0,10):
                if correctAnswers[i]==answers[i]:
                    marks=marks+1
            category=""
            if marks == 10:
                category="Legendary"
            elif marks>=8 and marks<=9:
                category="Titan"
            elif marks>=6 and marks<=7:
                category="Champion"
            elif marks>=4 and marks<=5:
                category="Gold"
            elif marks>=2 and marks<=3:
                category="Silver"
            elif marks>=0 and marks<=1:
                category="Bronze"

            Profile.objects.filter(username=n).update(marks=marks,category=category)
            return redirect("profile")
        return render(request,"code/test.html",{'questions':d})

def loginhandle(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("something went wrong")

def logouthandle(request):
    logout(request)
    return redirect("/")

def registerhandle(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            userr=User.objects.create_user(username,email,pass1)
            print(userr)
            userr.first_name=fname
            userr.last_name=lname
            userr.save()
            profile=Profile(name=fname,email=email,username=username)
            profile.save()
            return redirect("/")
    
    else:
            return HttpResponse("404-something went wrong")

def profile(request):
    username=request.user
    marks=Profile.objects.filter(username=username).first().marks
    intrest=Profile.objects.filter(username=username).first().intrest
    email=Profile.objects.filter(username=username).first().email
    category=Profile.objects.filter(username=username).first().category
    n=Profile.objects.filter(username=username).first().name
    param={
        'name':n,
        'username':username,
        'marks':marks,
        'intrest':intrest,
        'email':email,
        'category':category,
    }
    return render(request,"code/profile.html",param)

def buddylist(request):
    username=request.user
    category=Profile.objects.filter(username=username).first().category
    buddy=Profile.objects.filter(category=category).exclude(username=username)
    return render(request,"code/buddylist.html",{'buddy':buddy})

def budprofile(request,slug):
    bud=Profile.objects.filter(username=slug).first()
    
    return render(request,"code/budprofile.html",{'bud':bud})

def sendrequest(request,receiver):
    receiver_user = Profile.objects.get(username=receiver)
    sender=request.user
    sender_user=Profile.objects.get(username=sender.username)
    obj,created=ConnectRequest.objects.get_or_create(sender=sender_user,
        receiver=receiver_user,
        status="Pending"
    )
    return redirect("buddylist")

def cancelrequest(request):
    pass

def acceptrequest(request):
    pass

def declinerequest(request):
    pass
