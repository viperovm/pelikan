from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(verbose_name='Псевдоним')
    content = models.TextField(blank=True, verbose_name='Текст')
    excerpt = models.TextField(max_length=150, blank=True, verbose_name='Отрывок')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at', 'title']


class Review(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя пользователя')
    content = models.TextField(max_length=1050, blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at', '-id']


class Question(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='E-mail')
    content = models.TextField(max_length=1050, verbose_name='Вопрос')
    response = models.TextField(max_length=1050, blank=True, verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-created_at', '-id']

