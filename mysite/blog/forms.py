

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        '''
        Meta class tells django which model should be used to create this form.
        In this case, it is the Post Obj.
        '''
        model = Post
        fields = ('title', 'text', )  # this is a tuple, we tell django which
                                      # fields from Post must be exposed.


