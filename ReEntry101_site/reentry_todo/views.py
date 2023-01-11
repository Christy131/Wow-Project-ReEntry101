from django.shortcuts import render, redirect


from django.views import View
# Import model for Questions
from reentry_todo.models import Question, Comment
# Import question form
from reentry_todo.forms import QuestionForm, CommentForm, TagForm

# Create your views here.

# this is the homepage
class HomeView (View): 
    def get (self, request):
        return render(request=request, template_name='index.html')
# CommentDetailView is the question detail view about a particular question 
class QuestionDetailView(View):
    def get(self,request,question_id):
        # gets the question by the id
        question = Question.objects.get(id=question_id)
        # Filters all the comments associated with the question One to Many Relationship
        comment = Comment.objects.filter(question_id = question_id).order_by('-created_at')
        # Creates the view for the form
        comment_form = CommentForm(question_object = question) 
        current_tags = question.tags.all()
        tag_form = TagForm()
        html_data = {
            'question': question,
            'comment_list': comment,
            'comment_form': comment_form,
            'tag_form': tag_form,
            'tag_list': current_tags,
        }
        # What will be displayed on the DOM
        return render (
            request = request,
            template_name= 'details.html',
            context = html_data
        ) 
    def post(self, request, question_id):
        # Get the question by it's id
        comment = Question.objects.get(id=question_id)
        # Gets the commment and posts it to the question 
        comment_form = CommentForm(request.POST, question_object=comment)
        tag_form = TagForm(request.POST, comment)
        if 'add' in request.POST:
            comment_form.save()
        elif 'tag' in request.POST:
            tag_form.save(comment)
            # return redirect('question_detail', question_id)
        # Save the comment
        # Have to pass the question id because the comment is associated with the question so we needed to included question_id because we would get an error if we didn't include the question_id which is how we get to the question_detail page
        return redirect('question_detail', question_id)
        
# Viewing the questions all of them at once
class QuestionsView(View):
    def get(self, request):
        # Get all the questions
        questions = Question.objects.all()
        # Have the form displayed
        question_form = QuestionForm()
       
        html_data = {
             'question_list': questions,
             'question_form': question_form,
        }
        # Kite.html is where the user can enter in their question
        return render (
            request = request,
            template_name = 'kite.html',
            context = html_data
        )
    def post(self, request):
        # If the user clicks the add button, save it to add to the database
        question_form = QuestionForm(request.POST)
        question_form.save()
        tag_form = TagForm(request.POST)
        tag_form.save(question_form)
        return redirect('question')
#A function based view was created 
def delete(request, id):
    # Getting the comment id from the database
    comment= Comment.objects.get(id=id)
    # Comment is deleted
    comment.delete()
    return redirect('question')
        
class CommentView(View):
    def get(self, request, id):
        comment= Comment.objects.get(id=id)
        comment_form = CommentForm({'body':comment})

