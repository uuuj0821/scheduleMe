from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'password1', 'password2']
        labels = {
            'username' : '아이디',
            'full_name' : '이름',
            'password1' : '비밀번호',
            'password2' : '비밀번호 확인',
        }