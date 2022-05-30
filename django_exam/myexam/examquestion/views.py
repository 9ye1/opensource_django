from django.shortcuts import render, redirect
from .models import Question,Person

# Create your views here.
def maketest(request):
    if request.method == 'POST':
        mkt = Question()
        mkt.question = request.POST['question']
        mkt.choice1 = request.POST['choice1']
        mkt.choice2 = request.POST['choice2']
        mkt.choice3 = request.POST['choice3']
        mkt.choice4 = request.POST['choice4']
        mkt.choice5 = request.POST['choice5']
        mkt.answer = request.POST['answer']
        mkt.save()
        return redirect('maketest')
    elif(len(Question.objects.all()) >= 5):
        questionlist = Question.objects.all()
        return render(request, 'examquestion/exampage.html', {'questionlist': questionlist})
    else:
        mkt = len(Question.objects.all())
        return render(request, 'examquestion/maketestpage.html', {'mkt': mkt})

def exampage(request):
    if request.method == 'POST':
        answer = Person()
        answer.name = request.POST['name']
        answer.save()
        return redirect('exampage')
    else:
        questionlist = Question.objects.all()
        return render(request, 'examquestion/exampage.html', {'questionlist': questionlist})

def student(request):
    student_list = Person.objects.all()
    return render(request, 'examquestion/studentpage.html', {'student_list': student_list})

