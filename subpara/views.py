from django.shortcuts import render,redirect

from subpara.models import Article

# Create your views here.

def display(request):
    data = None
    if request.method == 'POST':
        search = request.POST.get('search')
        data = Article.objects.filter(heading__icontains = search)
    else:
        data = Article.objects.all().order_by('-id')
    context = {
        'data': data
    }
    return render(request,'index.html',context)

def ar(request,pk):
    data = Article.objects.get(id=pk)
    context = {
        'data1':data
    }
    return render(request,'detail.html',context)

def about(request):
    return render(request,'about.html')