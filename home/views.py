from django.shortcuts import render,HttpResponse,redirect
from home.models import Category, Codes
# Create your views here.
PASSWORD='DEEPak@123'
def home(request):
    snippets=[]
    cats=Category.objects.order_by('category').all()
    for cat in cats:
        cds=Codes.objects.filter(category=cat).all()
        if(len(cds)!=0):
            param={'name':cat.category,'codes':cds}
            snippets.append(param)
    params={'snippets':snippets,'categories':cats}
    return render(request,'index.html',params)

def addcategory(request):
    if(request.method=='POST'):
        category=request.POST['category']
        password=request.POST['password']
        if(password!=PASSWORD):
            return HttpResponse('Invalid user')
        try:
            category = Category(category=category)
            category.save()
        except Exception as e:
            return HttpResponse('Category already added')
        return redirect('addcode')

def addcode(request):
    if(request.method=="GET"):
        categories=Category.objects.order_by('category').all()
        params={'categories':categories}
        return render(request,'addcode.html',params)
    if(request.method=="POST"):
        category=request.POST['category']
        title=request.POST['title']
        code=request.POST['code']
        language=request.POST['language']
        password=request.POST['password']
        if(password!=PASSWORD):
            return HttpResponse('Invalid user')
        try:
            ctg=Category.objects.get(category=category)
            cd=Codes(category=ctg,title=title,code=code,language=language)
            cd.save()
        except Exception as e:
            return HttpResponse('Code can\'t be saved')
        return redirect('/')