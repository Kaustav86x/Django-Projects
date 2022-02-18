from wsgiref.util import request_uri
from django.shortcuts import render, redirect, HttpResponse
from student.models import Student

def index(request):
    # in order to have a html page, we need 'render' method 
    # return render(request, 'page.html')
    if request.method == "POST":
        nm = request.POST.get('name', '')
        rl = request.POST.get('roll', '')
        emd = request.POST.get('mail', '')
        pass1 = request.POST.get('pass1', '')
        pass2 = request.POST.get('pass2', '')
        if nm and emd and rl:
            if pass1 != pass2:
                return HttpResponse("Please confirm the password correctly !")
            else:
                student = Student(name = nm, roll = rl, email = emd, password = pass1)
                student.save()
                # print(request.POST)  (Tthis would print the content of the form on the console)
        else:
            return HttpResponse("Invalid Data. Please try again !")

    return render(request, 'page.html')
