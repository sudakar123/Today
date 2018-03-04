from django.shortcuts import render
from django.http import HttpResponse
from models import Question

# Create your views here.
def index(request):
    #return HttpResponse('welcome django')
    lq=Question.objects.order_by('-pub_date')[:5]
    op= ''.join(q.question_text for q in lq)
    return render(request,'polls/index.html',{'lq':lq})

def detail(request,qid):
    #return HttpResponse('The details of view: %s' %qid)
    question=Question.objects.get(pk=qid)
    return render(request,'polls/details.html',{'question':question})

def results(request,qid):
    return HttpResponse('The details of view: %s' %qid)


def vote(request,qid):
    return HttpResponse('The details of view: %s' %qid)

