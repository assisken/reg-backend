from django import forms


class LinuxPassResetForm(forms.Form):
    pwd = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Новый пароль',
        required=True
    )
    pwdcnf = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Подтвердите пароль',
        required=True
    )
