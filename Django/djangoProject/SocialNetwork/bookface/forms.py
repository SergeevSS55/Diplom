from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from .models import Photo, Comment
from django.core.validators import FileExtensionValidator

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Пароль")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label="Подтверждение пароля")
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата рождения'
    )
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name',
            'last_name', 'email', 'phone_number', 'birth_date'] # определяем поля для отображения в форме
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Email',
            'phone_number': 'Номер телефона',
        }


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError("Пароли не совпадают")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Хешируем пароль перед сохранением
        if commit:
            user.save()
        return user


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title', 'description']
        labels = {
            'image': 'Изображение',
            'title': 'Название',
            'description': 'Описание',
        }
        widgets = {
            'image': forms.FileInput()
        }
        validators = [
            FileExtensionValidator(['jpeg', 'jpg', 'png', 'gif']),
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Комментарий',
        }
        widgets = {
            'content': forms.Textarea(),
        }