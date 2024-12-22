from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    '''Создание модели CustomUser с расширением базовой модели AbstractUser
    (добавляем номер телефона и дату рождения)
    Редактирование административной панели'''
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True)
    birth_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    def __str__(self):
        """Переопределение строкового представления объекта.
        Возвращает имя и фамилию пользователя"""
        return f'{self.first_name} {self.last_name}'

    class Meta:
        """Определяем наименование в административной панеле"""
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Photo(models.Model):
    """Создание модели с описанием характеристик для загруженных фотографий.
    Данная модель сохраняет загруженные фотографии в директорию 'photos/',
    а также связывает фотографию с пользователем, который ее загрузил."""
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает название картинки,
        которое изначально дает пользователь"""
        return self.title


class Comment(models.Model):
    """Создание модели для хранения комментариев к фотографиям.
    Связывает комментарий с конкретной фотографией и пользователем,
    который его оставил."""
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Возвращает строковое представление,
        включающее имя пользователя и название фотографии"""
        return f"Комментарий от {self.user.username} на {self.photo.title}"
