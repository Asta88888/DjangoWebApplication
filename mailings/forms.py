from django.forms import ModelForm
from mailings.models import Recipient, Mailing, Message


class MailingForm(ModelForm):
    """Форма для модели Mailing. Позволяет создавать и редактировать рассылки."""
    class Meta:
        model = Mailing
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        """Инициализация формы и обновление атрибутов виджетов."""
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название рассылки'
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
    """Форма для модели Recipient. Позволяет создавать и редактировать получателей."""
    class Meta:
        model = Recipient
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        """Инициализация формы и обновление атрибутов виджетов."""
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите email получателя'
        })
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите Ф.И.О получателя'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите комментарий'
        })


class MessageForm(ModelForm):
    """Форма для модели Message. Позволяет создавать и редактировать сообщения."""
    class Meta:
        model = Message
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        """Инициализация формы и обновление атрибутов виджетов."""
        super().__init__(*args, **kwargs)
        self.fields['topic'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название сообщения'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите содержание сообщения'
        })
