from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # people=[
        
    #     {'name':'Nischay','age':'20'},
    #     {'name':'prabhash','age':'29'},
    #     {'name':'samdeep','age':'27'},
    #     {'name':'Ny','age':'16'},
    #     {'name':'Nsay','age':'20'},
    # ]
    # for man in people:
    #     if man['age']:
    #         print('ok')
    # vegetables=["carrot","spanish","potato"]
    # text= """orem ipsum dolor sit amet consectetur, adipisicing elit. Vo
    #                 luptatem veniam perferendis natus. Quod autem deserunt tempore sint ducimus explicabo in
    #                 cidunt ipsa commodi! Suscipit, velit nesciunt. Libero, alias fuga. Possimus provident accusantium aliquid dignissimos molestias, quos dol
    #                 ore nobis quaerat. Velit exercitationem sint aspernatur qua"""
    # hi= "sdaasdasd"
    return render(request,"index.html")

def about(request):
    context={"page":"about us"}
    return render(request,"About us.html",context)

def contact(request):
    context={"page":"contact"}
 
    return render(request,"contact.html",context)

def sucess_page(request):
    return HttpResponse("<h1>Sucess</h1>")