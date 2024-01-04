from django.shortcuts import render, redirect
from store.models import Product
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      phone = request.POST.get('phone') 
      desc = request.POST.get('desc')
      Contact = contact(name = name, email = email, phone = phone, desc = desc)
      Contact.save()
      messages.success(request, "Query Sent")
    return render(request, 'contact.html')