from django import forms
from django.core.exceptions import ValidationError

#from forum.models import Topic, Comment


class AddTopicForm(forms.ModelForm):
    subject = forms.CharField(label="Заголовок", max_length=100, min_length=7)
    first_comment = forms.CharField(label="Сообщение", widget=forms.Textarea())

    class Meta:
        #model = Topic
        fields = ['subject', 'first_comment']

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        #ALLOWED_SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-.?!+=/ '
        if len(subject) > 100:
            raise ValidationError("Длина превышает 100 символов")
        if len(subject) < 7:
            raise ValidationError("Слишком короткое заглавие, требуется не менее 7 символов")
        return subject


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(label="Текст комментария", max_length=2000, min_length=1, widget=forms.Textarea())

    class Meta:
        #model = Comment
        fields = ['content']
