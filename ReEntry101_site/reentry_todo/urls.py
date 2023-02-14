from django.urls import path

from reentry_todo.views import HomeView, QuestionDetailView, QuestionsView, CommentView, ResourceView,SearchView
# The single dot is a convention from command line applications. It means the current directory. In terms of Django it stands for the directory/module the current file is on.
from . import views
#just to commit 
urlpatterns=[
    # This path is the homepage
    path ('', HomeView.as_view(), name='home'),
    # This is the question view
    path('questions', QuestionsView.as_view(), name ='question'),
    # This is the question with the comments, so the question is listed at the top and the comments connected is below the question
    path('<int:question_id>', QuestionDetailView.as_view(), name="question_detail"),
    # This is a function based view was created 
    path('delete/<int:id>', views.delete, name='delete'),
    # Takes the comment to a new page to update it
    path('comment/<int:id>', CommentView.as_view(), name='comment'),
    # Take the user to the resources page
    path('resources', ResourceView.as_view(), name ='resources'),
    path('search_results', SearchView.as_view(), name='search_results')
]