from django.shortcuts import render
from django.http import HttpResponse
from models import Question

# Create your views here.
def index(request):
    #return HttpResponse('welcome django')
    lp=Question.objects.order_by('-pub_date')[:5]
    output=','.join(q.question_text for q in lp)
    #return HttpResponse(output)
    return render(request,'polls/index.html',{'lp':lp})

def detail(request,qid):
    #return HttpResponse('The details of view %s' %qid)
    question=Question.objects.get(pk=qid)
    return render(request,'polls/detail.html',{'question':question})

def results(request,qid):
    return HttpResponse('The results of view %s' %qid)

def vote(request,qid):
    return HttpResponse('The vote of view %s' %qid)

