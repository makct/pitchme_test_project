from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Topic, City


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(
        label="Город проведения", queryset=City.objects.all(), empty_label=None
    )
    start_interval = forms.DateField(
        label="Начало интервала",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        required=False,
    )
    end_interval = forms.DateField(
        label="Конец интервала",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
        required=False,
    )
    topic = forms.ModelChoiceField(
        label="Тема встречи", queryset=Topic.objects.all(), empty_label=None
    )
