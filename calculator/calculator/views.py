from django import http
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def calculator(request):
    num1= float(request.POST.get('num1'))
    num2= float(request.POST.get('num2'))
    opcode= request.POST.get('opcode')

    result=0

    if(opcode=='+'):
        result =num1+num2
    elif(opcode=='-'):
        result =num1-num2
    elif(opcode=='*'):
        result =num1*num2
    elif(opcode=='/'):
        result =num1/num2
    elif(opcode=='^'):
        result =num1**num2

    data={'output':result,'num1':num1, 'num2':num2}

    return render(request, 'index.html', data)

def reset(request):
    data={'output':"",'num1':"", 'num2':""}
    return render(request,'index.html', data)

