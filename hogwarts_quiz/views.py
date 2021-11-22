from django.shortcuts import render, redirect
import csv
import random
from django.http import HttpResponse
from .models import Quiz
from .models import Result
from .models import House


# HMTL Page Views


# Home Page (home.html)
def home(request):
    # Collect all houses for introduction on Home page
    context = {}
    houses = House.objects.all()
    context['houses'] = houses

    return render(request,
                  'hogwarts_quiz/home.html',
                  context=context)


# Sorting Page (sorting.html) => Handling Sorting Quiz logic
def sorting(request):
    context = {}

    # Setting boolean values for conditional display of sections on html page
    # (by default, quiz starter section is visible)
    context['game_start'] = True
    context['game_on'] = False
    context['game_end'] = False

    # Selecting quiz from db and format quiz name for showing as site title
    quiz = Quiz.objects.filter(name='sorting_ceremony').first()
    questions_count = quiz.questions.all().count()
    context['quiz'] = quiz
    context['quiz_name'] = firstletter_uppercase(quiz.name)

    # Handling click on Start Sorting button
    if 'sorting_start' in request.POST:
        # Setting house values to zero
        context['gryffindor_count'] = 0
        context['hufflepuff_count'] = 0
        context['ravenclaw_count'] = 0
        context['slytherin_count'] = 0

        # Setting boolean values to display quiz game section
        context['game_start'] = False
        context['game_on'] = True

        # Select first question with related answers of quiz to start
        curr_question = quiz.questions.filter(number=1).first()
        context['current_question'] = curr_question
        context['answers'] = curr_question.answers.all()

        return render(request,
                      'hogwarts_quiz/sorting.html',
                      context=context)

    # Handling click on Next Question button
    if 'next_question' in request.POST:
        # Setting boolean values to display quiz game section
        context['game_start'] = False

        # Getting result house values so far
        gryffindor_count = check_point_empty(request.POST['count_gryffindor'])
        hufflepuff_count = check_point_empty(request.POST['count_hufflepuff'])
        ravenclaw_count = check_point_empty(request.POST['count_ravenclaw'])
        slytherin_count = check_point_empty(request.POST['count_slytherin'])

        # Getting result house value of current answer
        # and increment related house's points
        selected_answer = request.POST.get('answers_options')
        if 'gryffindor' == selected_answer:
            gryffindor_count = add_housepoint(gryffindor_count)
        elif 'hufflepuff' == selected_answer:
            hufflepuff_count = add_housepoint(hufflepuff_count)
        elif 'ravenclaw' == selected_answer:
            ravenclaw_count = add_housepoint(ravenclaw_count)
        else:
            slytherin_count = add_housepoint(slytherin_count)

        # Setting result house values with current answer's values included
        context['gryffindor_count'] = gryffindor_count
        context['hufflepuff_count'] = hufflepuff_count
        context['ravenclaw_count'] = ravenclaw_count
        context['slytherin_count'] = slytherin_count

        # Get current question index
        current_index = int(request.POST['current_index'])
        # Saving result to database
        # if current question index = last question number
        if current_index == questions_count:
            # Get house selected by user in last question
            selected = selected_answer

            # Transform result house values
            # to percentage based on total number of questions
            gryffindor_point = int(point_to_percentage(gryffindor_count,
                                                       questions_count))
            hufflepuff_point = int(point_to_percentage(hufflepuff_count,
                                                       questions_count))
            ravenclaw_point = int(point_to_percentage(ravenclaw_count,
                                                      questions_count))
            slytherin_point = int(point_to_percentage(slytherin_count,
                                                      questions_count))

            # Get maximum house percentage and select house(s) for final result
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
            # Create result object in database
            result = Result.objects.create(quiz=quiz.name,
                                           result=result_house.strip(),
                                           selected_house=selected,
                                           gryffindor=gryffindor_point,
                                           hufflepuff=hufflepuff_point,
                                           ravenclaw=ravenclaw_point,
                                           slytherin=slytherin_point)

            # Get newly created result object's id for result display
            # and set boolean values to display quiz end section
            context['result_id'] = result.id
            context['game_on'] = False
            context['game_end'] = True

            return render(request,
                          'hogwarts_quiz/sorting.html',
                          context=context)

        # If current question index
        # != last question number, increment current question index
        index = current_index + 1
        # Set boolean values to display quiz game section
        context['game_on'] = True
        # Select next question based
        # on incremented current index with related answers
        curr_question = quiz.questions.filter(number=index).first()
        context['current_question'] = curr_question
        context['answers'] = curr_question.answers.all()

        return render(request,
                      'hogwarts_quiz/sorting.html',
                      context=context)

    # Handling click on See My House button
    if 'end_quiz' in request.POST:
        # Passing current game's result's ID to sorting result display page
        id = request.POST['result_id']
        return redirect('sorting-result', id=id)

    return render(request,
                  'hogwarts_quiz/sorting.html',
                  context=context)


def sorting_result(request, id):
    context = {}
    # Select result with related id from database
    result_house = Result.objects.filter(id=id).first()
    context['result'] = result_house
    # Format Page title and house result title
    context['quiz'] = firstletter_uppercase(result_house.quiz)
    context['title'] = firstletter_uppercase(result_house.result)
    # Get result houses based on result
    context['houses'] = get_result_house(result_house.result)
    # Get other houses based on result
    context['other_houses'] = get_other_house(result_house.result)

    # Handle user satisfaction input
    # and conditional display of satisfaction-related sections on html page
    context['satisfaction_done'] = False

    # If satisfaction input already provided
    if result_house.satisfaction is not None:
        context['satisfaction_done'] = True
        # If satisfaction input already provided & positive input received
        if result_house.satisfaction == 'yes':
            context['satisfied'] = True
            context['satisfaction_comment'] = \
                'So glad that you are satisfied with your house! ' \
                'Wander around and discover!'
        else:
            # If satisfaction input already provided & negative input received
            context['satisfied'] = False
            context['satisfaction_comment'] = \
                'Sorry you are not satisfied ' \
                '- you may try again and think again your answers!'

    # Handle user click on Yes button (satisfied)
    # => Alter result to update 'satisfaction' field,
    #    handle conditional display and set user satisfaction input comment
    if 'satisfied_btn' in request.POST:
        result_house.satisfaction = "yes"
        result_house.save()
        context['satisfaction_done'] = True
        context['satisfied'] = True
        context['satisfaction_comment'] = \
            'So glad that you are satisfied with your house! ' \
            'Wander around and discover!'
        return render(request,
                      'hogwarts_quiz/sorting-result.html',
                      context=context)

    # Handle user click on No button (not satisfied)
    # => Alter result to update 'satisfaction' field,
    #    handle conditional display and set user satisfaction input comment
    if 'not_satisfied_btn' in request.POST:
        result_house.satisfaction = "no"
        result_house.save()
        context['satisfaction_done'] = True
        context['satisfied'] = False
        context['satisfaction_comment'] = \
            'Sorry you are not satisfied ' \
            '- you may try again and think again your answers!'
        return render(request,
                      'hogwarts_quiz/sorting-result.html',
                      context=context)

    # Handle user click on Save My Result button
    # => Export current result to csv file via http response
    if 'save_result' in request.POST:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = \
            'attachment; filename="my_result.csv"'

        writer = csv.writer(response)
        writer.writerow(['quiz',
                         'result',
                         'selected house',
                         'gryffindor',
                         'hufflepuff',
                         'ravenclaw',
                         'slytherin',
                         'satisfaction'])

        writer.writerow([result_house.quiz,
                         result_house.result,
                         result_house.selected_house,
                         result_house.gryffindor,
                         result_house.hufflepuff,
                         result_house.ravenclaw,
                         result_house.slytherin,
                         result_house.satisfaction])
        return response

    return render(request,
                  'hogwarts_quiz/sorting-result.html',
                  context=context)


def results(request):
    context = {}
    # Collect all houses for displaying results
    houses = House.objects.all()
    # Update house statistics based on latest results
    update_statistics(houses, len(houses))
    context['houses'] = houses

    # Handle click on Save All Results button
    # => Export current displayed results to csv file via http response
    if 'save_results' in request.POST:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = \
            'attachment; filename="all_result.csv"'

        writer = csv.writer(response)
        writer.writerow(['name',
                         'students',
                         'selected in house',
                         'selected by others',
                         'satisfaction rate',
                         'gryffindor rate',
                         'hufflepuff rate',
                         'ravenclaw rate',
                         'slytherin rate'])

        for h in houses:
            writer.writerow([h.name,
                             h.students,
                             h.selected,
                             h.selected_others,
                             h.satisfaction_rate,
                             h.gryffindor,
                             h.hufflepuff,
                             h.ravenclaw,
                             h.slytherin])
        return response

    return render(request,
                  'hogwarts_quiz/results.html',
                  context=context)


def house(request, name):
    context = {}
    # Select first house from database based on house name
    current_house = House.objects.filter(name=name).first()
    # Update house statistics based on latest results
    update_statistics(current_house, 1)
    context['house'] = current_house

    # Open 'quotes.txt' file and read in lines (quotes from it)
    f = open('static/txt/quotes.txt', 'r')
    lines = f.readlines()
    f.close()
    # Sort quotes in array for selected house based on house name
    house_quotes = []
    for line in lines:
        if current_house.name in line:
            house_quotes.append(line)
    # Set up a random number selection for the range of selected quotes' array
    quote_num = random.randint(0, (len(house_quotes)-1))
    # Select a quote from quotes' array based on randomly selected index
    context['quote'] = house_quotes[quote_num].split('_')[1]
    context['quote_author'] = house_quotes[quote_num].split('_')[2]

    return render(request,
                  'hogwarts_quiz/house.html',
                  context=context)


# Helper functions


# Turn first letter to upper case for quiz name / result house(s)
# => Used in page views sorting / sorting_result
def firstletter_uppercase(name):
    final_name = ''
    if '_' in name:
        # Transform quiz name (sorting_ceremony)
        name_array = name.split('_')
        for word in name_array:
            firstchar = word[0].upper()
            wo_firstchar = word[1:]
            final_name += firstchar + wo_firstchar + ' '
        return final_name.strip()
    elif ' ' in name:
        # Transform multiple house results to result title
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
        # Transform single house result to result title
        firstchar = name[0].upper()
        wo_firstchar = name[1:]
        final_name += 'House ' + firstchar + wo_firstchar
        return final_name.strip()


# Increment house point with one
# => Used in page view sorting
def add_housepoint(count):
    return int(count) + 1


# Convert request.post result to number
# => Used in page view sorting
def check_point_empty(point):
    # If request.post number value is null, return 0, else converted number
    if point == '':
        return 0
    else:
        return int(point)


# Convert result points to percentage
# => Used in page view sorting
# + helper function get_all_results (used for results / house page views)
def point_to_percentage(point, total):
    number = int(point) / total * 100
    return round(number, 0)


# Return array of result houses based on result string
# => Used in page view sorting_result
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


# Return array of other than result houses based on result string
# => Used in page view sorting_result
def get_other_house(result_house):
    houses = House.objects.all()
    other_houses = []
    for h in houses:
        if h.name not in result_house:
            other_houses.append(h)

    return other_houses


# Updating one house's / all houses' statistics based on actual database values
# => Used in page views house and results
def update_statistics(houses, count):
    if count > 1:
        # If input consists of more houses (page view results)
        for h in houses:
            results_statistics = get_all_results(h.name)

            h.students = results_statistics[0]
            h.selected = results_statistics[1]
            h.selected_others = results_statistics[2]
            h.satisfaction_rate = results_statistics[3]
            h.gryffindor = results_statistics[4]
            h.hufflepuff = results_statistics[5]
            h.ravenclaw = results_statistics[6]
            h.slytherin = results_statistics[7]
            h.save()
    else:
        # If input consists of only one house (page view house)
        results_statistics = get_all_results(houses.name)

        houses.students = results_statistics[0]
        houses.selected = results_statistics[1]
        houses.selected_others = results_statistics[2]
        houses.satisfaction_rate = results_statistics[3]
        houses.gryffindor = results_statistics[4]
        houses.hufflepuff = results_statistics[5]
        houses.ravenclaw = results_statistics[6]
        houses.slytherin = results_statistics[7]
        houses.save()


# Helper function for above update_statistics function based on given house
def get_all_results(house):
    # Initialize numeric house values
    count = 0
    others_count = 0
    selected = 0
    selected_others = 0
    not_satisfied = 0
    satisfied = 0
    satisfaction = 0
    gryffindor_result = 0
    hufflepuff_result = 0
    ravenclaw_result = 0
    slytherin_result = 0

    # Loop through all results in database
    all_results = Result.objects.all()
    for r in all_results:
        if house in r.result:
            # If given house is in the result
            count += 1
            # Collect sub-houses percentage values
            gryffindor_result += r.gryffindor
            hufflepuff_result += r.hufflepuff
            ravenclaw_result += r.ravenclaw
            slytherin_result += r.slytherin

            # If current house selected by user and got sorted in it
            if r.selected_house in r.result:
                selected += 1
            # If user is satisfied with sorting result
            if 'yes' == r.satisfaction:
                satisfied += 1
            # If user is not satisfied with sorting result
            if 'no' == r.satisfaction:
                not_satisfied += 1
        else:
            # If given house is not in the result
            others_count += 1
            # # If the given house selected by user bot not sorted in it
            if house in r.selected_house:
                selected_others += 1

    # Turn numeric house values to result percentages
    # => As division by zero throws error, divisor check before execution
    if count > 0:
        selected = int(point_to_percentage(selected, count))
        gryffindor_result = round(gryffindor_result / count)
        hufflepuff_result = round(hufflepuff_result / count)
        ravenclaw_result = round(ravenclaw_result / count)
        slytherin_result = round(slytherin_result / count)

    if others_count > 0:
        selected_others = int(point_to_percentage(selected_others,
                                                  others_count))

    if (satisfied+not_satisfied) > 0:
        satisfaction = int(point_to_percentage(satisfied,
                                               (satisfied+not_satisfied)))

    # Passing new percentage values as array to function update_statistics
    counts = [count,
              selected,
              selected_others,
              satisfaction,
              gryffindor_result,
              hufflepuff_result,
              ravenclaw_result,
              slytherin_result]

    return counts
