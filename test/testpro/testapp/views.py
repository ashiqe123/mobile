from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import test
from .forms import mobile_form
# Create your views here.
def home(request):
    mobile=test.objects.all()
    context={
        'mobile_list':mobile
    }
    return render(request,'home.html',context)
def detail(request,mobile_id):
    mobile=test.objects.get(id=mobile_id)
    return render(request,'detail.html',{'mobile':mobile})

def add(request):
    if request.method=='POST':
        type=request.POST['type']
        brand=request.POST['brand']
        model=request.POST['model']
        desc=request.POST['desc']
        img=request.FILES['img']
        testadd=test(brand=brand,type=type,model=model,desc=desc,img=img)
        testadd.save()
        messages.info(request,"added succesfully !!!")


    return render(request,'add.html')
def update(request,id):
    mobile=test.objects.get(id=id)
    form=mobile_form(request.POST or None, request.FILES,instance=mobile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'mobile':mobile})
def delete(request,id):
    if request.method=='POST':
        dele=test.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render(request,'delete.html')