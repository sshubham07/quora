from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()

    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'form': form, 'questions': questions})

def recent_questions(request):
    questions = Question.objects.order_by('-created_at')[:10]
    return render(request, 'recent_questions.html', {'questions': questions})

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'question': question, 'form': form})
