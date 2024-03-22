from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Question
from .models import Choice

# Create your views here.

def index(request):
    latest_quest_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_quest_list": latest_quest_list}
    
    return render(request, "poll/index.html", context)

def prueba(request):
    
    return HttpResponse("esto es la mama de la mama")

def detail(request, question_id):
    try:
        
        operadores = { 
        "question" : Question.objects.get(pk=question_id),
        "choices" : Choice.objects.filter(question= question_id)
    }
    except Question.DoesNotExist:
        
        raise Http404("Question does not exist")
        
    return render(request, "poll/details.html", operadores) 

def results(request, question_id):
    response = "You're looking at the results of question %s."
    
    return HttpResponse(response % question_id)

def vote(request, question_id):
    
    return HttpResponse("You're voting on question %s." % question_id)

