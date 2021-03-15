from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
def home(request):
    
    if(request.session['AllInput'] != "Guest"):
        return render(request, 'homepage.html',{'name':request.session['AllInput']})
    return render(request, 'homepage.html',{'name':'Guest'})
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['loginname']
        password = request.POST['loginpass']
        user = auth.authenticate(username = username, password =password  )
        if user is not None:
            request.session['AllInput'] = username
            auth.login(request , user)
            print("Login !!!")
            return redirect('home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request, 'login.html')
    
def register(request):
    if request.method == 'POST':
        print('run')
        email = request.POST['emailReg']
        username = request.POST['usernameReg']
        password= request.POST['passwordReg']
        user = User.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('login')
    return render(request,'register.html')
