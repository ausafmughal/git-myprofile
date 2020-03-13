from django.shortcuts import render
from .models import posts, Contacts
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        your_name = request.POST.get('name')
        your_email = request.POST.get('email')
        your_website = request.POST.get('website')
        your_message = request.POST.get('message')

        var_contact = Contacts(name=your_name,email=your_email,webs=your_website,message=your_message)
        var_contact.save()

    return render(request, 'contact.html', )

def blogs(request):
    b = posts.objects.all()
    return render(request,'blogs.html',{'b':b})