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
    context = {}
    quiz = Quiz.objects.filter(name='Sorting Ceremony').first()
    serializer = QuizSerializer(quiz)
    data = JSONRenderer().render(serializer.data)
    context['quiz'] = quiz
    context['quiz_json'] = data.decode()

    if request.method == "POST":
        resultMaxPoint = request.POST['result-maxpoint']
        resultSelectedHouse = request.POST['result-selectedhouse']
        resultGryffindor = request.POST['result-gryffindor']
        resultHufflepuff = request.POST['result-hufflepuff']
        resultRavenclaw = request.POST['result-ravenclaw']
        resultSlytherin = request.POST['result-slytherin']

        resultHouse = ''
        resultComment = ''
        if resultGryffindor == resultMaxPoint:
            resultHouse += 'Gryffindor '
            house = House.objects.filter(name='Gryffindor').first()
            resultComment += house.keywords
        if resultHufflepuff == resultMaxPoint:
            resultHouse += 'Hufflepuff '
            house = House.objects.filter(name='Hufflepuff').first()
            resultComment += house.keywords
        if resultRavenclaw == resultMaxPoint:
            resultHouse += 'Ravenclaw '
            house = House.objects.filter(name='Ravenclaw').first()
            resultComment += house.keywords
        if resultSlytherin == resultMaxPoint:
            resultHouse += 'Slytherin'
            house = House.objects.filter(name='Slytherin').first()
            resultComment += house.keywords

        result = Result.objects.create(quiz=quiz.name,
                                       result=resultHouse,
                                       comment = resultComment,
                                       selected_house=resultSelectedHouse,
                                       gryffindor=resultGryffindor,
                                       hufflepuff=resultHufflepuff,
                                       ravenclaw=resultRavenclaw,
                                       slytherin=resultSlytherin)

        return redirect('sorting-result', id=result.id)
    else:
        return render(request, 'hogwarts_quiz/sorting.html', context=context)


def sorting_result(request, id):
    context = {}

    result_house = Result.objects.filter(id=id).first()
    context['result'] = result_house

    houses = []
    title_house = ''
    if len(result_house.result) <= 10:
        title_house += 'House ' + result_house.result.strip()
        house = House.objects.filter(name=result_house.result.strip()).first()
        houses.append(house)
    else:
        title_house += 'Houses '
        result_houses = result_house.result.split(' ')
        for h in result_houses:
            house = House.objects.filter(name=h.strip()).first()
            houses.append(house)
            if h == result_houses[-1]:
                title_house += h.strip()
            else:
                title_house += h.strip() + ' & '
    context['title'] = title_house
    context['houses'] = houses

    return render(request, 'hogwarts_quiz/sorting-result.html', context=context)


def results(request):
    return render(request, 'hogwarts_quiz/results.html', {})


def feedback(request):
    return render(request, 'hogwarts_quiz/feedback.html', {})