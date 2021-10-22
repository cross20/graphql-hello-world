import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):
    all_quizzes = graphene.List(QuizzesType)
    all_questions = graphene.List(QuestionType)

    def resolve_all_quizzes(root, info):
        return Quizzes.objects.all()
    
    def resolve_all_questions(root, info):
        return Question.objects.all()

schema = graphene.Schema(query=Query)