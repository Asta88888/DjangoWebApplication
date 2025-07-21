from django.forms import ModelForm
from mailings.models import Recipient, Mailing, Message


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите название рассылки'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['recipients'].widget.attrs.update({
            'class': 'form-control'
        })


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RecipientForm).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите email получателя'
        })
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите Ф.И.О получателя'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите комментарий'
        })


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(MessageForm).__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите название сообщения'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'Введите содержание сообщения'
        })