import graphene
from graphene_django import DjangoObjectType
from .models import Quizzes, Category, Question, Answer

# Querys
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "date_created")

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
    category = graphene.Field(CategoryType, id=graphene.Int())
    # field allows one return value
    quiz = graphene.Field(QuizzesType, id=graphene.Int())
    # field allows one return value
    question = graphene.Field(QuestionType, id=graphene.Int())
    # list allows multiple return values
    question_answers = graphene.List(AnswerType, questionId=graphene.Int())

    def resolve_category(root, info, id):
        # get allows one return value
        return Category.objects.get(pk=id)

    def resolve_quiz(root, info, id):
        # get allows one return value
        return Quizzes.objects.get(pk=id)

    def resolve_question(root, info, id):
        # get allows one return value
        return Question.objects.get(pk=id)

    def resolve_question_answers(root, info, questionId):
        # filter allows multiple return values
        return Answer.objects.filter(question=questionId)

# Mutations
class NewCategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name) # create new category
        category.save()
        return NewCategoryMutation(category=category)

class NewQuizMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        #category = graphene.InputObjectType(Category) # TODO: implement category
        date_created = graphene.DateTime(required=True)

    quiz = graphene.Field(QuizzesType)

    @classmethod
    def mutate(cls, root, info, title, date_created): # TODO: implement category
        quiz = Quizzes(title=title, date_created=date_created)
        quiz.save()
        return NewQuizMutation(quiz=quiz)

class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(id=id)
        category.name = name # update name of category
        category.save()
        return UpdateCategoryMutation(category=category)

class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return

class Mutation(graphene.ObjectType):
    new_category = NewCategoryMutation.Field()
    new_quiz = NewQuizMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()

# CRUD (Create, Read, Update, Delete)
schema = graphene.Schema(query=Query, mutation=Mutation)