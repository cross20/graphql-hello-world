import graphene
from graphene_django import DjangoObjectType
from .models import Quiz, Category, Question, Answer

# Querys
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
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
    quiz = graphene.Field(QuizType, id=graphene.Int())
    # field allows one return value
    question = graphene.Field(QuestionType, id=graphene.Int())
    # list allows multiple return values
    answer = graphene.List(AnswerType, questionId=graphene.Int())

    def resolve_category(root, info, id):
        # get allows one return value
        return Category.objects.get(pk=id)

    def resolve_quiz(root, info, id):
        # get allows one return value
        return Quiz.objects.get(pk=id)

    def resolve_question(root, info, id):
        # get allows one return value
        return Question.objects.get(pk=id)

    def resolve_answer(root, info, questionId):
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
        categoryPk = graphene.Int(required=True)

    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, title, categoryPk):
        quiz = Quiz(title=title, category=Category.objects.get(pk=categoryPk))
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

class UpdateQuizMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=False)
        categoryPk = graphene.Int(required=False)

    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        quiz = Quiz.objects.get(id=id)
        quiz.title = kwargs.get('title', quiz.title)
        quiz.category = Category.objects.get(pk=kwargs.get('categoryPk', quiz.category.id))
        quiz.save()
        return UpdateQuizMutation(quiz=quiz)

class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return

class DeleteQuizMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    quiz = graphene.Field(QuizType)

    @classmethod
    def mutate(cls, root, info, id):
        quiz = Quiz.objects.get(id=id)
        quiz.delete()
        return

class Mutation(graphene.ObjectType):
    new_category = NewCategoryMutation.Field()
    new_quiz = NewQuizMutation.Field()
    update_category = UpdateCategoryMutation.Field()
    update_quiz = UpdateQuizMutation.Field()
    delete_category = DeleteCategoryMutation.Field()
    delete_quiz = DeleteQuizMutation.Field()

# CRUD (Create, Read, Update, Delete)
schema = graphene.Schema(query=Query, mutation=Mutation)