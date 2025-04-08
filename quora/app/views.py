from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all().order_by('-created_at')
    form = AnswerForm()

    # Get all answer IDs liked by current user
    liked_answer_ids = Like.objects.filter(user=request.user, answer__in=answers).values_list('answer_id', flat=True)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect('question_detail', question_id=question.id)

    return render(request, 'question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form,
        'liked_answer_ids': liked_answer_ids
    })


@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)

    if not created:
        # User already liked, so unlike
        like.delete()

    return HttpResponseRedirect(reverse('question_detail', args=[answer.question.id]))
