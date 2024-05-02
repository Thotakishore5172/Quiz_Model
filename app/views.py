from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse,JsonResponse

def home(request):
    courses =Course.objects.all()
    d={'courses':courses}
    return render(request,'home.html',d)

def api_question(request,id):
    raw_questions=Question.objects.filter(course=id)[:20]
    questions=[]

    for raw_question in raw_questions:
        question={}
        question['question']=raw_question.question
        question['answer']=raw_question.answer

        options=[]

        options.append(raw_question.option_one)
        options.append(raw_question.option_two)
        if raw_question.option_three !='':
            options.append(raw_question.option_three)
        if raw_question.option_four !='':
            options.append(raw_question.option_four)

        question['options']=options

        questions.append(question)
    return JsonResponse(questions,safe=False)
        

def take_quiz(request,id):
    d={'id':id}
    return render(request,'quiz.html',d)

def login(request):
   
    return render(request,'login.html')