from django.shortcuts import render,redirect
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from . models import *
import joblib

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def login2(request):
    template=loader.get_template('login2.html')
    return HttpResponse(template.render())
def sign(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))
def back(request):
    return redirect('login2')
def back2(request):
    return redirect('predict')
def createuser(request):
    users = request.POST['username']
    password1 = request.POST['password1']
    email = request.POST['email']
    password2= request.POST['password2']

    if password1 == password2:
        load = signup(username = users,password = password1,email = email)
        load.save()
        return redirect('login2')
    else:
        return HttpResponse("pasword are not match")
    
def signin(request):
    email = request.POST['emailid']
    password = request.POST['pass']
    data = signup.objects.filter(email=email)
    if data:
        data = signup.objects.get(email=email)
        if data.password == password:
            return redirect('predict')
        else:
            return render(request,"password.html")
    else:
        # return HttpResponse("Incorect password")
        return render(request,"username.html")
def predict(request):
    template=loader.get_template('predict.html')
    return HttpResponse(template.render())
def username(request):
    template=loader.get_template('username.html')
    return HttpResponse(template.render())
def output(request):
    template=loader.get_template('output.html')
    return HttpResponse(template.render())
def result(request):
    # Load the scikit-learn model
    try: 
        model= joblib.load('C:/Users/Student/Desktop/django-Placement_render-master/app1/finalized_model.sav')
    except FileNotFoundError:
        return HttpResponse("Model file not found. Please check the file path.")

    # Get the input data from the request
    input_data = [float(request.GET.get(key, 0.0)) for key in ['age', 'gender', 'stream', 'internship', 'cgpa', 'hostel', 'historyofbacklog']]

    # Check if all required features are provided
    if len(input_data) != 7:
        return HttpResponse("Please provide values for all features.")

    # Make prediction
    try:
        ans = model.predict([input_data])
    except ValueError:
        return HttpResponse("Error occurred during prediction. Please check the input data.")

    # return render(request, "output.html", {'ans': ans[0], 'lis': input_data})
    val1 = int(request.GET['n1'])
    val2 = int(request.GET['n2'])
    val3 = int(request.GET['n3'])
    val4 = int(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = int(request.GET['n6'])
    val7 = int(request.GET['n7'])
    pred = model.predict([[val1, val2, val3,val4, val5, val6, val7]])
    result1 = ""
    if pred == [0]:
        result1 = "You are not placed !."
    else:
        result1 = "You are placed !!!!!."
    return render(request, "output.html",
                  {"result2": result1})
def index1(request):
    s=Data1.objects.all().values()
    output=" "
    for x in s:
        output+=x["age"]+x["gender"]+x["stream"]+x["internships"]+x["cgpa"]+x["hostel"]+["historyofbacklog"]
    return HttpResponse(output)
def index2(request):
    s=Data1.objects.all().valus()
    template=loader.get_template(data.html)
    context={
        's':s,
    }
    return HttpResponse(template.render(context,request))
def data(request):
    s=Data1.objects.all().values()
    output=" "
    return render(request,'data.html',{'s': s})
def addrecord(request):
    x=request.POST['age']
    y=request.POST['gender']
    t=request.POST['stream']
    m=request.POST['internships']
    s=request.POST['cgpa']
    h=request.POST['hostel']
    j=request.POST['historyofbacklog']
    member=Members(age=x,gender=y,stream=t,internships=m,cgpa=s,hostel=h,historyofbacklog=j)
    member.save()
    return HttpResponseRedirect(reverse)