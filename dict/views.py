from django.shortcuts import render
from . import services
# Create your views here.
def index(request):
    return render(request,'index.html')

def word(request):
    search=request.GET.get('search')
    res=services.get_meaning("en_US",search)
    try:
        res=res[0]['meanings']
        context={
            "res":res
        }
    except:
        res=[]
        context={
            "res":res
        }
    return render(request,'word.html',context)


