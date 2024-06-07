from django.shortcuts import render,redirect
from Backend.models import Catdb,Productdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contactdb
from django.contrib import messages

# Create your views here.
def index_page(request):
    return render(request,"index.html")
def new_category(request):
    return render(request,"Add_category.html")
def save_page(request):
    if request.method=="POST":
        na=request.POST.get('name')
        de=request.POST.get('desc')
        img=request.FILES['image']
        obj=Catdb(name=na,desc=de,image=img)
        obj.save()
        messages.success(request,"Category Saved Suucessfully")
        return redirect(new_category)


def display_category(request):
    data=Catdb.objects.all()
    return render(request,"view_cat.html",{'data':data})

def edit_cat(request,catid):
    data=Catdb.objects.get(id=catid)
    return render(request,"edit_cat.html",{'data':data})

def update_cat(request,catid):
    if request.method=="POST":
        na = request.POST.get('name')
        de = request.POST.get('desc')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Catdb.objects.get(id=catid).image
        Catdb.objects.filter(id=catid).update(name=na,desc=de,image=file)
        messages.success(request,"Updated Successfully")
        return redirect(display_category)

def delete_cat(reuest,catid):
    x=Catdb.objects.filter(id=catid)
    x.delete()
    messages.error(reuest,"Deleted Success")
    return redirect(display_category)



def login_page(request):
    return render(request,"login.html")
def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pas=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pas)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pas
                messages.success(request,"Welcome")
                return redirect(index_page)
            else:
                messages.error(request,"Invalid Password..!")
                return redirect(login_page)
        else:
            messages.warning(request,"User not Found ")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout Succesfully")
    return redirect(login_page)

def product_page(request):
    data=Catdb.objects.all()
    return render(request,"product.html",{'data':data})
def save_pro(request):
    if request.method=="POST":
        cna=request.POST.get('cname')
        pna=request.POST.get('pname')
        des=request.POST.get('desc')
        pr=request.POST.get('price')
        img = request.FILES['pimage']
        obj=Productdb(cname=cna,pname=pna,desc=des,price=pr,pimage=img)
        obj.save()
        messages.success(request,"Product Saved Successfully")
        return redirect(product_page)

def display_pro(request):
    data=Productdb.objects.all()
    return render(request,"display_pro.html",{'data':data})

def edit_pro(request,pid):
    data=Catdb.objects.all()
    dat=Productdb.objects.get(id=pid)
    return render(request,"edit_pro.html",{'data':data,'dat':dat})

def update_pro(request,pid):
    if request.method=="POST":
        cna=request.POST.get('cname')
        pna=request.POST.get('pname')
        des=request.POST.get('desc')
        pr=request.POST.get('price')
        try:
            img=request.FILES['pimage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Productdb.objects.get(id=pid).pimage
        Productdb.objects.filter(id=pid).update(cname=cna,pname=pna,desc=des,price=pr,pimage=file)
        return redirect(display_pro)

def delete_pro(request,pid):
    data=Productdb.objects.filter(id=pid)
    data.delete()
    messages.error(request, "Product Deleted Successfully")
    return redirect(display_pro)



def contact_details(request):
   con=Contactdb.objects.all()
   return render(request,"Contactdata.html",{'con':con})

def delete_contact(request,cid):
    data=Contactdb.objects.filter(id=cid)
    data.delete()
    return redirect(contact_details)

