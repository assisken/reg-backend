from django.core.validators import RegexValidator
from django import forms


class LinuxUser(forms.Form):
    linux_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'student123'}),
        label='Имя пользователя',
        required=True,
        max_length=30,
        validators=[RegexValidator(regex=r'^[a-z]([a-z0-9-]{0,31}|[a-z0-9-]{0,30}\$)$')]
    )
    pwd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Пароль',
        required=True
    )
    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
        required=True
    )
