from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup

# Create your views here.
def index(request):
    return HttpResponse("Test URL")
def sayHello(request,name):
    return HttpResponse(f'Hello {name}')

def times2 (request,multiply):
    return HttpResponse(f'The product of {multiply} x 2 = {multiply*2}')

def total (request,number):
    countdown=number
    sum=0
    for x in range (number):
        sum+= int(countdown)
        countdown-=1
    return HttpResponse(f'The sum of all numbers from 0 to {number} is {sum}')

#Both methods will be called in one function
def newCup(request):

    #Class Method
    def Cup1():
        newCup1= Cup (name = "Kenn's Cup",material = "Styrofoam",manufactuerDate = '2019-2-3')
        newCup1.save()
        return HttpResponse(newCup1)
    def Cup2():
        newCup2=Cup (name = "Erin's Cup",material = "Plastic",manufactuerDate = '2012-10-13')
        newCup2.save()
        return HttpResponse(newCup2)
    def Cup3():
        newCup3=Cup (name = "Kenn's Cup",material = "Styrofoam",manufactuerDate = '2019-2-3')
        newCup3.save()
        return HttpResponse(newCup3)

    #Create Method
    def createCup1():
        cCup1=Cup.objects.create(name = "Donald Trump's Cup",material = "Aluminum",manufactuerDate = '1978-12-15')
        return HttpResponse(cCup1)
    def createCup2():
        cCup2=Cup.objects.create(name = "Jussie Smollet's Cup",material = "Paper",manufactuerDate = '2001-5-30')
        return HttpResponse(cCup2)
    def createCup3():
        cCup3=Cup.objects.create(name = "James Brown's Cup",material = "Tin",manufactuerDate = '1989-9-11')
        return HttpResponse(cCup3)

   #Calls each seperate cup
    Cup1()
    Cup2()
    Cup3()
    createCup1()
    createCup2()
    createCup3()
    return HttpResponse()

def allPurchase(request):
    allCups=Cup.objects.all()
    for x in allCups:
        print(f'Cup:{x.name}') #prints cup name
        print(f'ManufactureDate:{x.manufactuerDate}') #prints manufacture date
        print('\n') #adds a newline in between
    return HttpResponse()

def newMaterial(request):

    allCups=Cup.objects.all()
    for y in Cup.objects.filter(manufactuerDate__gt='2012-12-31'): #checks for cups after this date
            y.material="Slightly New" #changes material to 'Slightly new'
            y.save() #saves entry
    for x in allCups: #prints for test results
        print(f'{x.name}')
        print(f'{x.material}')
        print(f'{x.manufactuerDate}')
        print('\n')
    return HttpResponse()

def all (request):
    allCups=Cup.objects.all()
    cupafter2012= Cup.objects.filter(manufactuerDate__gt = 2012-12-31)
    context= {
        'allCups':allCups,
        'cupafter2012':cupafter2012,
    }

    return render(request,'cupApp.index.html',context)