from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, name, age):
    return HttpResponse("<h1>Hello {}, y´re {} years old.</h1>".format(name, age))

# View to addd numbers
def somar(request, num1, num2):
    soma = num1 + num2
    return HttpResponse("A soma entre <b>{}</b> e <b>{}</b> é: <b>{}</b>".format(num1, num2, soma))