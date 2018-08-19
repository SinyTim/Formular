from django import forms


class EmailForm(forms.Form):
    sender = forms.EmailField(label='Ваш email:')
    subject = forms.CharField(max_length=100, label='Тема:')
    message = forms.CharField(widget=forms.Textarea, label='Текст:')
    cc_myself = forms.BooleanField(required=False, label='Выслать копию сообщения:')
