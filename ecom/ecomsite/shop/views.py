from django.shortcuts import render
from .models import Products , Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products_objects = Products.objects.all()
    # search code
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        products_objects = products_objects.filter(title__icontains=item_name)
        
        #paginator code
    paginator = Paginator(products_objects,4)
    page = request.GET.get('page')
    products_objects = paginator.get_page(page)
        
    return render(request,'shop/index.html',{'product_objects':products_objects})

def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})
def checkout(request):
    if request.method =="POST":
        items = request.POST.get('items','')
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address',"")
        city =request.POST.get('city',"")
        state=request.POST.get('state',"")
        zipcode=request.POST.get('zipcode',"")
        total= request.POST.get('total',"")
        order = Order(name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,items=items, total=total)    
        order.save()
    return render(request,'shop/checkout.html')