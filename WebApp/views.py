from django.shortcuts import render,redirect
from Backend.models import Productdb,Catdb
from WebApp.models import Contactdb,Registerdb,Cartdb
from django.contrib import messages

# Create your views here.
def home_page(req):
    cat=Catdb.objects.all()
    return render(req,"home.html",{'category':cat})
def about_page(req):
    cat = Catdb.objects.all()
    return render(req,"about.html",{'category':cat})
def contact_page(req):
    cat = Catdb.objects.all()
    return render(req,"contact.html",{'category':cat})
def save_contact(request):
    if request.method=="POST":
        na=request.POST.get('name')
        eml=request.POST.get('email')
        msg=request.POST.get('message')
        sub=request.POST.get('subject')
        mob=request.POST.get('mobile')
        obj=Contactdb(name=na,email=eml,message=msg,subject=sub,mobile=mob)
        obj.save()
        return redirect(contact_page)
def our_product(req):
    cat = Catdb.objects.all()
    data=Productdb.objects.all()
    return render(req,"ourproducts.html",{'data':data,'category':cat})

def products_filtered(req,cat_name):
    cat = Catdb.objects.all()
    data=Productdb.objects.filter(cname=cat_name)
    return render(req,"Products_filtered.html",{'data':data,'category': cat})

def singleproduct(request,proid):
    cat = Catdb.objects.all()
    data=Productdb.objects.get(id=proid)
    return render(request,"single_product.html",{'data':data,'category':cat})

def register(req):
    return render(req,"register.html")

def save_reg(req):
    if req.method=="POST":
        nam=req.POST.get('username')
        eml=req.POST.get('email')
        pas=req.POST.get('pass1')
    obj=Registerdb(name=nam,email=eml,password=pas)
    if Registerdb.objects.filter(name=nam).exists():
        messages.warning(req,"Username Already Exists")
    elif Registerdb.objects.filter(email=eml).exists():
        messages.warning(req,"Email Id Already Exists")
    else:
        obj.save()
        messages.success(req,"sucessfully Registered")
    return redirect(register)

    obj.save()
    return redirect(register)

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass')
        if Registerdb.objects.filter(name=un,password=pswd).exists():
            request.session['name']=un
            request.session['password']=pswd
            messages.success(request,"Log In Successfull")
            return redirect(home_page)
        else:
            return redirect(register)
    else:

        return redirect(register)

def user_logout(request):
   del  request.session['name']
   del  request.session['password']
   messages.success(request, "Log Out Successfully")
   return redirect(home_page)

def save_cart(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        prodname=request.POST.get('productname')
        qty=request.POST.get('quantity')
        total=request.POST.get('totalprice')
        obj=Cartdb(uname=uname,productname=prodname,quantity=qty,totalprice=total)
        obj.save()
        messages.success(request, "Item Added to Cart Successfully")
        return redirect(home_page)

def cart_page(request):
    # uname from cartdb
    cat = Catdb.objects.all()
    data=Cartdb.objects.filter(uname=request.session['name'])
    total=0
    for d in data:
        total+=d.totalprice
    return render(request,"cartpage.html",{'data':data,'category':cat,'total':total})

def delete_item(request,pid):
    x=Cartdb.objects.filter(id=pid)
    x.delete()
    messages.success(request, "Item Deleted from the Cart Successfully")
    return redirect(cart_page)

def user_page(request):
    return render(request,"userpage.html")