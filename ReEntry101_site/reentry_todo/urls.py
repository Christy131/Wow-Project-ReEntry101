from django.urls import path

from reentry_todo.views import HomeView

urlpatterns=[
    path ('', HomeView.as_view(), name='home'),

]