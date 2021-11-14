from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer
from .models import Answer
from .models import Question
from .models import Quiz
from .models import QuizSerializer
from .models import Result
from .models import House


def home(request):
    houses = House.objects.all()
    context = {'houses': houses}
    return render(request, 'hogwarts_quiz/home.html', context=context)


def sorting(request):
    return render(request, 'hogwarts_quiz/sorting.html', {})


def results(request):
    return render(request, 'hogwarts_quiz/results.html', {})


def feedback(request):
    return render(request, 'hogwarts_quiz/feedback.html', {})