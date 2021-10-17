from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .models import Question
# Create your views here.

def index(request):
    latest_questions=Question.objects.order_by('-pub_date')[:5]
    return render(request,'polls/index.html',{'latest_questions':latest_questions})

def details(request,question_id):
    #question=Question.objects.get(pk=1)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detials.html',{'question':question})
    #return HttpResponse("This is the details view of the question {}".format(question_id))

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    #return HttpResponse("There are the results of the Questions {}".format(question_id))

def votes(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try :
        print(request.POST['choice'])
        selected_choices=question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,'polls/detials.html',{'question':question,'error_message':'Please select a choice'})
    else:
        selected_choices.votes+=1
        selected_choices.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

