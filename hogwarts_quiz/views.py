from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer
from .models import Answer
from .models import Question
from .models import Quiz
from .models import QuizSerializer
from .models import Result
from .models import House


def home(request):
    context = {}
    houses = House.objects.all()
    context['houses'] = houses
    return render(request, 'hogwarts_quiz/home.html', context=context)


def sorting(request):
    context = {}

    context['game_start'] = True
    context['game_on'] = False
    context['game_end'] = False

    quiz = Quiz.objects.filter(name='sorting_ceremony').first()
    questions_count = quiz.questions.all().count()
    context['quiz'] = quiz
    context['quiz_name'] = firstletter_uppercase(quiz.name)

    if 'sorting_start' in request.POST:
        context['gryffindor_count'] = 0
        context['hufflepuff_count'] = 0
        context['ravenclaw_count'] = 0
        context['slytherin_count'] = 0

        context['game_start'] = False
        context['game_on'] = True

        curr_question = quiz.questions.filter(number=1).first()
        context['current_question'] = curr_question
        context['answers'] = curr_question.answers.all()

        return render(request, 'hogwarts_quiz/sorting.html', context=context)

    if 'next_question' in request.POST:
        context['game_start'] = False

        gryffindor_count = check_point_empty(request.POST['count_gryffindor'])
        hufflepuff_count = check_point_empty(request.POST['count_hufflepuff'])
        ravenclaw_count = check_point_empty(request.POST['count_ravenclaw'])
        slytherin_count = check_point_empty(request.POST['count_slytherin'])

        selected_answer = request.POST.get('answers_options')
        if 'gryffindor' == selected_answer:
            gryffindor_count = add_housepoint(gryffindor_count)
        elif 'hufflepuff' == selected_answer:
            hufflepuff_count = add_housepoint(hufflepuff_count)
        elif 'ravenclaw' == selected_answer:
            ravenclaw_count = add_housepoint(ravenclaw_count)
        else:
            slytherin_count = add_housepoint(slytherin_count)

        context['gryffindor_count'] = gryffindor_count
        context['hufflepuff_count'] = hufflepuff_count
        context['ravenclaw_count'] = ravenclaw_count
        context['slytherin_count'] = slytherin_count

        current_index = int(request.POST['current_index'])
        if current_index == questions_count:
            selected = selected_answer
            gryffindor_point = int(point_to_percentage(gryffindor_count, questions_count))
            hufflepuff_point = int(point_to_percentage(hufflepuff_count, questions_count))
            ravenclaw_point = int(point_to_percentage(ravenclaw_count, questions_count))
            slytherin_point = int(point_to_percentage(slytherin_count, questions_count))

            houses_points = {
                "gryffindor": gryffindor_point,
                "hufflepuff": hufflepuff_point,
                "ravenclaw": ravenclaw_point,
                "slytherin": slytherin_point,
            }

            max_point = max(houses_points.values())

            result_house = ''
            for k, v in houses_points.items():
                if v == max_point:
                    result_house += (k+' ')

            result = Result.objects.create(quiz=quiz.name,
                                           result=result_house.strip(),
                                           selected_house=selected,
                                           gryffindor=gryffindor_point,
                                           hufflepuff=hufflepuff_point,
                                           ravenclaw=ravenclaw_point,
                                           slytherin=slytherin_point)
            context['result_id'] = result.id
            context['game_on'] = False
            context['game_end'] = True

            return render(request, 'hogwarts_quiz/sorting.html', context=context)

        index = current_index + 1

        context['game_on'] = True
        curr_question = quiz.questions.filter(number=index).first()
        context['current_question'] = curr_question
        context['answers'] = curr_question.answers.all()

        return render(request, 'hogwarts_quiz/sorting.html', context=context)

    if 'end_quiz' in request.POST:
        id = request.POST['result_id']
        return redirect('sorting-result', id=id)

    return render(request, 'hogwarts_quiz/sorting.html', context=context)


def sorting_result(request, id):
    context = {}

    result_house = Result.objects.filter(id=id).first()
    context['result'] = result_house
    context['quiz'] = firstletter_uppercase(result_house.quiz)
    context['title'] = firstletter_uppercase(result_house.result)
    context['houses'] = get_result_house(result_house.result)
    context['other_houses'] = get_other_house(result_house.result)

    return render(request, 'hogwarts_quiz/sorting-result.html', context=context)


def results(request):
    return render(request, 'hogwarts_quiz/results.html', {})


def feedback(request):
    return render(request, 'hogwarts_quiz/feedback.html', {})


def firstletter_uppercase(name):
    final_name = ''
    if '_' in name:
        name_array = name.split('_')
        for word in name_array:
            firstchar = word[0].upper()
            wo_firstchar = word[1:]
            final_name += firstchar + wo_firstchar + ' '
        return final_name.strip()
    elif ' ' in name:
        final_name += 'Houses '
        result_houses = name.split(' ')
        for h in result_houses:
            firstchar = h[0].upper()
            wo_firstchar = h[1:]
            if h == result_houses[-1]:
                final_name += firstchar + wo_firstchar + ' '
            else:
                final_name += firstchar + wo_firstchar + ' & '
        return final_name.strip()
    else:
        firstchar = name[0].upper()
        wo_firstchar = name[1:]
        final_name += firstchar + wo_firstchar
        return final_name.strip()


def add_housepoint(count):
    return int(count) + 1


def check_point_empty(point):
    if point == '':
        return 0
    else:
        return int(point)


def point_to_percentage(point, total):
    number = int(point) / total * 100
    return round(number, 0)


def get_result_house(result_house):
    houses = []
    houses_string = result_house.strip()
    if ' ' in houses_string:
        result_houses = houses_string.split(' ')
        for h in result_houses:
            house = House.objects.filter(name=h.strip()).first()
            houses.append(house)
    else:
        house = House.objects.filter(name=houses_string).first()
        houses.append(house)

    return houses


def get_other_house(result_house):
    houses = House.objects.all()
    other_houses = []
    for h in houses:
        if h.name not in result_house:
            other_houses.append(h)

    return other_houses


