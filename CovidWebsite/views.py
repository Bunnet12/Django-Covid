from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
import psycopg2
def home(request):
    
    return render(request, 'homepage.html',{'name':request.session['AllInput']})
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST['loginname']
        password = request.POST['loginpass']
        user = auth.authenticate(username = username, password =password  )
        if user is not None:
            request.session['AllInput'] = username
            auth.login(request , user)
            print("Login !!!")
            print(User.objects.all() )
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
def symptoms(request):   
    score = 0
    status = ''
    for i in range(1,6):
        if request.POST.get('select'+str(i)) == 'option1':
            score+=1
    print(score)
    if(score >= 4):
        status = 'Severe, You must go to hospital now https://www.pasteur-kh.org/'
        request.session['status'] = status
    elif(score ==3):
        status = 'Not Severe But you should go to check at hospital'  
        request.session['status'] = status
    else:
        status = 'Normal' 
        request.session['status'] = status
    return render(request, 'symptom.html', {'status': status})

def account(request):
    
    return render(request, 'account.html',{'name':request.session['AllInput'],'status':request.session['status']})