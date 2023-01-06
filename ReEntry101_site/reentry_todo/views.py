from django.shortcuts import render, redirect


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
    def post(self, request, question_id):
        comment = Question.objects.get(id=question_id)
        comment_form = CommentForm(request.POST, question_object=comment)
        comment_form.save()
        redirect('comment_detail', question_id)
        if 'update' in request.POST: 
            comment.save()
        if 'delete' in request.POST:
            comment.delete()
        return redirect('comment_detail', question_id)
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
             'question_form': question_form
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
        return redirect('question')
        
        