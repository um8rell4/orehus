from django import forms
from .models import OrehusChange, CustomUser, UserZodiacSign
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Ваш орех, пожалуйста!', help_text=' ', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='Паспорт!', widget=forms.PasswordInput(attrs={'class': 'form-control '
                                                                                            'form-control-lg'}))


class OrehusForms(forms.ModelForm):
    # comment = forms.CharField(max_length=100, required=False, label='Комментарий')
    # operation = forms.IntegerField(label='Сколько')
    # orehus_user = forms.ModelChoiceField(queryset=OrehusUsers.objects.all(), label='Кому')
    class Meta:
        model = OrehusChange
        fields = ['comment', 'operation', 'orehus_user']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'operation': forms.TextInput(attrs={'class': 'form-control'}),
            'orehus_user': forms.Select(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    unchanged_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    bio = forms.CharField(label='О себе', required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                       'rows': 8}))
    birth_date = forms.DateField(label='Дата рождения', input_formats=['%d.%m.%Y'], widget=forms.DateInput(
        attrs={
        'class':
                                                                                                   'form-control'}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':
                                                                                                    'form-control form-control-lg'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'unchanged_name', 'bio', 'birth_date', 'password1', 'password2')


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'user_vk_url', 'user_zodiac', 'birth_date', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'user_vk_url': forms.URLInput(attrs={'class': 'form-control', 'type': 'text',
                                                                'placeholder': 'ссылка на '
                                                                                                         'вк'}),
            'user_zodiac': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':
            'dd-mm-yyyy'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'О себе', }),
        }
