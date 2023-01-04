from django.urls import path

from reentry_todo.views import HomeView, CommentDetailView, QuestionsView

urlpatterns=[
    path ('', HomeView.as_view(), name='home'),
    path('questions', QuestionsView.as_view(), name ='question'),
    path('<int:question_id>', CommentDetailView.as_view(), name="comment_detail"),
]