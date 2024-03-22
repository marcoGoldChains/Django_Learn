from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


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
    
    operadores = { 
        "question" : Question.objects.get(pk=question_id),
        "choices" : Choice.objects.filter(question= question_id)
    }
    
    return render(request, "poll/results.html", operadores)

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    
    except (KeyError, Choice.DoesNotExist):
    
        return render(request, "poll/detail.html", {"question":question, "error_message":"you didn't select a choice"})
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("poll:results", args=(str(question.id))))