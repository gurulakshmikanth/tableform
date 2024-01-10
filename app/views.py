from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length
def display_topics(request):
    QLTO=Topics.objects.all()
    QLTO=Topics.objects.all().order_by('topic_name')
    
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def insert_topics(request):
    tn=input('enter name')
    nto=Topics.objects.get_or_create(topic_name=tn)[0]
    nto.save()
    QLTO=Topics.objects.all()


    d={'topics':QLTO}
    return render(request,'display_topics.html',d)


def insert_webpage(request):
    tn=input('topicname')
    n=input('name')
    u=input('url')
    email=input('email')
    to=Topics.objects.get(topic_name=tn)
    nwo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=email)[0]
    nwo.save()
    QLTO=Webpage.objects.all()
    d={'web':QLTO}
    return render(request,'display_webpage.html',d)

def display_webpage(request):
    QLTO=Webpage.objects.all()
    QLTO=Webpage.objects.all().order_by(Length('name'))
    
    QLTO=Webpage.objects.filter(Q(topic_name='cricket') | Q(url__endswith='in'))
    d={'web':QLTO}
    return render(request,'display_webpage.html',d)


def display_acces(request):
    QLTO=AccesRecords.objects.all()
    QLTO=AccesRecords.objects.filter()
    d={'acces':QLTO}
    return render(request,'display_acces.html',d)

    



def insert_acces(request):
    pk=int(input('pk'))
    
    d=input('date')
    a=input('author')
    ao=Webpage.objects.get(pk=pk)
    nao=AccesRecords.objects.get_or_create(name=ao,date=d,author=a)[0]
    nao.save()
    QLTO=AccesRecords.objects.all()
    d={'acces':QLTO}
    return render(request,'display_acces.html',d)

def update_webpage(request):
    #Webpage.objects.filter(topic_name='cricket').update(name='rohith')
    #Webpage.objects.filter(email='dohni@gmail.com').update(name='dohni')
    CTO=Topics.objects.get_or_create(topic_name='kabaddi')[0]
    CTO.save()
    Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'manjith'})
    QLWO=Webpage.objects.all()
    d={'web':QLWO}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    Webpage.objects.filter(name='dohni').delete()
    QLTO=Webpage.objects.all()
    d={'web':QLTO}
    return render(request,'display_webpage.html',d)