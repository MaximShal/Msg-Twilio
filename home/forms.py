from django import forms


class MessageForm(forms.Form):
    phone = forms.CharField(label='Номер телефону', max_length=15,
                                   help_text='Впишіть номер телефону в форматі: +1234567890')
    message = forms.CharField(label='Повідомлення', widget=forms.Textarea)
