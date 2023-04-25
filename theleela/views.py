import datetime
from django.shortcuts import render
import mysql.connector as sql
def home(request):
    if(request.method=="POST"):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        m=sql.connect(host="localhost",user="root",passwd="jayesh10",database="emp")
        cursor=m.cursor()
        username=request.POST.get("username")
        password=request.POST.get("password")
        department=request.POST.get("department")
        date=datetime.datetime.now()
        print(username)
        print(password)
        print(department)
        print(date)
        c="insert into emprecord values('{}','{}','{}')".format(username,department,date)
        cursor.execute(c)
        m.commit()
        

    return render(request,"index.html",{})
def addemp(request):
    return render(request,"addemp.html",{})
def admin(request):
    return render(request,"admin.html",{})
