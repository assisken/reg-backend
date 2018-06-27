from django import forms


class LinuxPassResetForm(forms.Form):
    pwd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Новый пароль',
        required=True,
    )
    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': ''}),
        label='Подтвердите пароль',
        required=True
    )


class DatabasePassForm(forms.Form):
    pwd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль для базы данных',
        required=True
    )
    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
        required=True
    )


class DbSelectMultipleForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = tuple((i, '{}_{}'.format(user.linux_user, i+1)) for i in range(5))
        self.fields['select'].widget = forms.SelectMultiple(
            choices=options, attrs={'class': 'form-control'}
        )

    select = forms.MultipleChoiceField(label='Список доступных баз данных')

# OPTIONS = tuple((i, ''.format()) for i in range(5))
# select = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=OPTIONS)
