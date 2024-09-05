from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("This is Homepage")

    context = { "variable" : "my"
               }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def contact(request):
    if request.method == "POST":
        pass
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")


def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")
