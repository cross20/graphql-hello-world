import graphene
from graphene.types.structures import List
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
        fields = ("id", "title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):
    # field allows one return value
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    # list allows multiple return values
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        # get allows one return value
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        # filter allows multiple return values
        return Answer.objects.filter(question=id)

schema = graphene.Schema(query=Query)