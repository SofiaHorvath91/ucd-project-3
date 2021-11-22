from django.db import models
from rest_framework import serializers


# Answer object (actual answer + associated house)
class Answer(models.Model):
    answer = models.TextField(blank=True, null=True)
    house = models.TextField(blank=True, null=True)
    pass


# Serialize answers for Question object
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        depth = 1


# Question object (related quiz, number, actual question, associated answers)
class Question(models.Model):
    number = models.IntegerField(blank=True, null=True)
    quiz = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answer, related_name='answers', blank=True)
    pass


# Passing serialized answers to Question object & serialize questions for Quiz object
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
        depth = 2


# Quiz object (quiz name, quiz description, associated questions with answers)
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)


# Passing serialized questions to Quiz object
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'
        depth = 2


# Result object (related quiz, sub-results / houses, house selected by user, final house(s), user result satisfaction)
class Result(models.Model):
    quiz = models.CharField(max_length=255, blank=True, null=True)
    gryffindor = models.IntegerField(blank=True, null=True)
    hufflepuff = models.IntegerField(blank=True, null=True)
    ravenclaw = models.IntegerField(blank=True, null=True)
    slytherin = models.IntegerField(blank=True, null=True)
    selected_house = models.TextField(max_length=50, blank=True, null=True)
    result = models.CharField(max_length=600, blank=True, null=True)
    satisfaction = models.CharField(max_length=600, blank=True, null=True)


# House object
# => Descriptive : Name, keywords, intro poem, symbol, element, personality traits, founder, common room, ghost
# => Quantitative : number of students, selection rate in house, selection rate in other houses,
#                   average user result satisfaction rate, sub-results / houses
class House(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.TextField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    symbol = models.TextField(max_length=1000, blank=True, null=True)
    element = models.TextField(max_length=1000, blank=True, null=True)
    traits = models.TextField(max_length=5000, blank=True, null=True)
    founder = models.TextField(max_length=5000, blank=True, null=True)
    commonroom = models.TextField(max_length=5000, blank=True, null=True)
    ghost = models.TextField(max_length=1000, blank=True, null=True)
    students = models.IntegerField(blank=True, null=True)
    selected = models.IntegerField(blank=True, null=True)
    selected_others = models.IntegerField(blank=True, null=True)
    satisfaction_rate = models.IntegerField(blank=True, null=True)
    gryffindor = models.IntegerField(blank=True, null=True)
    hufflepuff = models.IntegerField(blank=True, null=True)
    ravenclaw = models.IntegerField(blank=True, null=True)
    slytherin = models.IntegerField(blank=True, null=True)