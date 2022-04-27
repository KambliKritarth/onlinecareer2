from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def myform(request):
    return render(request,'myform.html')

def careeroptions(request):
    return render(request,'careeroptions.html')

def aptitude(request):
    return render(request,'aptitude.html')

def aptitude_cse(request):
    return render(request,'aptitude_cse.html')

def aptitude_extc(request):
    return render(request,'aptitude_extc.html')

def contact(request):
    model = Contact
    all_contacts = Contact.objects.all
    name = request.POST.get('name',"Anonymous")
    user_contact = request.POST.get('contact',"Contactless")
    user_query = request.POST.get('query',"Queryless")
    ins = Contact(name=name,contact = user_contact,query = user_query)
    ins.save()
    print(name)
    return render(request, 'contact.html')