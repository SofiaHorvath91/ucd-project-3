from django.db import models
from rest_framework import serializers


class Answer(models.Model):
    answer = models.TextField(blank=True, null=True)
    house = models.TextField(blank=True, null=True)
    pass


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        depth = 1


class Question(models.Model):
    quiz = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    answers = models.ManyToManyField(Answer, related_name='answers', blank=True)
    pass


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
        depth = 2


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'
        depth = 2


class Result(models.Model):
    quiz = models.CharField(max_length=255, blank=True, null=True)
    gryffindor = models.IntegerField(blank=True, null=True)
    hufflepuff = models.IntegerField(blank=True, null=True)
    ravenclaw = models.IntegerField(blank=True, null=True)
    slytherin = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=600, blank=True, null=True)
    comment = models.TextField(max_length=1000, blank=True, null=True)


class House(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    name_smallcaps = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    symbol = models.TextField(max_length=1000, blank=True, null=True)
    element = models.TextField(max_length=1000, blank=True, null=True)
    traits = models.TextField(max_length=5000, blank=True, null=True)
    founder = models.TextField(max_length=5000, blank=True, null=True)
    commonroom = models.TextField(max_length=5000, blank=True, null=True)
    ghost = models.TextField(max_length=1000, blank=True, null=True)
    students = models.IntegerField(blank=True, null=True)
    gryffindor = models.IntegerField(blank=True, null=True)
    hufflepuff = models.IntegerField(blank=True, null=True)
    ravenclaw = models.IntegerField(blank=True, null=True)
    slytherin = models.IntegerField(blank=True, null=True)
