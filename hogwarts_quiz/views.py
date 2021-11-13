from django.shortcuts import render, redirect


def home(request):
    return render(request, 'hogwarts_quiz/home.html', {})


def sorting(request):
    return render(request, 'hogwarts_quiz/sorting.html', {})


def results(request):
    return render(request, 'hogwarts_quiz/results.html', {})


def feedback(request):
    return render(request, 'hogwarts_quiz/feedback.html', {})