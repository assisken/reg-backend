from django import forms

from .models import Database
from main.models import User


class LinuxPassResetForm(forms.Form):
    pwd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Новый пароль',
        required=True,
    )
    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
        required=True
    )


class DbPassResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['db_password']
        widgets = {
            'db_password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'db_password': 'Пароль'
        }

    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
        required=True
    )

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('db_password')
        pwdcnf = cleaned_data.get('pwdcnf')
        if pwd != pwdcnf:
            raise forms.ValidationError('Пароли не совпадают.')


class DatabaseForm(forms.ModelForm):
    class Meta:
        model = Database
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название БД',
        }


class DbSelectMultipleForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = ((db.pname, db.name) for db in Database.objects.filter(owner=user))
        self.fields['select'].widget = forms.Select(
            choices=options, attrs={'class': 'form-control'}
        )

    select = forms.MultipleChoiceField(label='')
