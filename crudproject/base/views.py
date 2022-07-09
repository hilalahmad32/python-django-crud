from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from base.models import Product

# Create your views here.
def index(request):
    products=""
    if request.GET.get('search') != "":
        products=Product.objects.filter(title=request.GET.get('search'))
    else:
        products=Product.objects.all()
    paginator=Paginator(products,1)
    page=request.GET.get('page',1)
    page_obj=paginator.page(page)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context={'products': products,'page_obj':page_obj}
    return render(request, 'index.html',context)

def create(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        content=request.POST.get('content')
        product=Product(title=title,price=price,content=content)
        product.save()
        return redirect('/')
    else:
        return render(request, 'create.html')

def edit(request,id):
    products=Product.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        content=request.POST.get('content')
        products.title=title
        products.price=price
        products.content=content
        products.save()
        return redirect('/')
    else:
        context={
            'products':products
        }
        return render(request, 'edit.html',context)

def delete(request,id):
    products=Product.objects.get(id=id)
    products.delete()
    return redirect('/')
