from django.shortcuts import render

from django.views import View
# Import model for Questions
from reentry_todo.models import Question, Comment
# Import question form
from reentry_todo.forms import QuestionForm, CommentForm

# Create your views here.

# this is the homepage
class HomeView (View): 
    def get (self, request):
        return render(request=request, template_name='index.html')
# CommentDetailView is the question detail view about a particular question 
class CommentDetailView(View):
    def get(self,request,question_id):
        # need question model first
        question = Question.objects.get(id=question_id)
        comment = Comment.objects.filter(question_id = question_id)
        comment_form = CommentForm(question_object = question) 
        html_data = {
            'question': question,
            'comment_list': comment,
            'comment_form': comment_form
        }
        return render (
            request = request,
            template_name= 'details.html',
            context = html_data
        ) 
    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        comment_form = CommentForm(request.POST, instance= comment)
        if 'update' in request.POST: 
            comment_form.save()
        elif 'delete' in request.POST:
            comment.delete()
        # elif 'add' in request.POST:
        #     comment_form = CommentForm(request.POST, task_object = task)
        #     comment_form.save()
        #     return redirect('task_detail', task.id)
# Viewing the questions all of them at once
class QuestionsView(View):
    def get(self, request):
        questions = Question.objects.all()
        question_form = QuestionForm()
        html_data = {
             'question_list': questions,
             'form': question_form
        }
        return render (
            request = request,
            template_name = 'kite.html',
            context = html_data
        )
    def post(self, request):
        question_form = QuestionForm(request.POST)
        question_form.save()
        # Needs a redirect from a pathway
        # return redirect()
        
        