from django.forms import ModelForm
from reentry_todo.models import Question, Comment

class QuestionForm(ModelForm):
    '''
    creating a question form the input box and the field required is called description
    '''
    class Meta:
        model = Question
        fields = ['question']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
    def __init__(self, *args,**kwargs):
        question = kwargs.pop('question_object')
        super().__init__(*args,**kwargs)
        # This needs to be created still on a seperate view
        self.instance.question = question
        self.fields['body'].label=''


