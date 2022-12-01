from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.shortcuts import redirect,render

from.models import *
def index(request):
    posts=KZ.objects.all()
    cats=Category.objects.all()
    context={
        'posts':posts,
        'cats':cats,
        'title':"Главная страница",
        'cat_selected':0,
    }
    return render(request,'kz/index.html',context=context)

def about(request):
    return render(request,'kz/about.html',{'title':'Про Казахстан'})

def contact(request):
    return HttpResponse("edil.zhadil@mail.ru")

def review(request):
    return HttpResponse("Будем рады только хорошим отзывам!")

def tour(request):
    return HttpResponse("Советуем Sunday.Tours!")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Братан иди поспи</h1>')

def show_post(request,post_id):
    return HttpResponse(f"Статья={post_id}")

def show_category(request,cat_id):

    posts = KZ.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts)==0:
        raise Http404()
    context = {
        'posts': posts,
        'cats': cats,
        'title': "Отоброжение по рубрикам",
        'cat_selected': cat_id,
    }
    return render(request, 'kz/index.html', context=context)