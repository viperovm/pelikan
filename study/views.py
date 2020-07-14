from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .forms import QuestionForm
from django.core.paginator import Paginator

from .models import *


class Posts(ListView):
    model = Post
    template_name = 'study/blog.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class SinglePost(DetailView):
    model = Post
    template_name = 'study/post.html'
    context_object_name = 'post'
    # slug_url_kwarg = 'post_slug'


class Reviews(ListView):
    model = Review
    template_name = 'study/review.html'
    context_object_name = 'items'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отзывы'
        return context

    def get_queryset(self):
        return Review.objects.filter(is_published=True)


# class Questions(ListView):
#     model = Question
#     template_name = 'study/question.html'
#     context_object_name = 'items'
#     paginate_by = 2
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Вопросы и ответы'
#         context['form'] = QuestionForm()
#         return context
#
#     def get_queryset(self):
#         return Question.objects.filter(is_published=True)


# class Questions(FormMixin, ListView):
#     model = Question
#     template_name = 'study/question.html'
#     context_object_name = 'items'
#     form_class = QuestionForm
#     paginate_by = 2
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Вопросы и ответы'
#         context['form'] = QuestionForm()
#         return context
#
#     def get_object(self):
#         pass
#
#     def get_queryset(self):
#         return Question.objects.filter(is_published=True)
#
#     def post(self, request, *args, **kwargs):
#         """ Обработка POST при использовани FormMixin в DetailView """
#         self.object = self.get_object()
#         form = self.get_form()
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class Questions(FormMixin, ListView):
    model = Question
    context_object_name = 'items'
    template_name = 'study/question.html'
    paginate_by = 2
    form_class = QuestionForm
    success_url = 'study/question.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вопросы и ответы'
        context['form'] = QuestionForm()
        return context

    def get_queryset(self):
        return Question.objects.filter(is_published=True)

    def get(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            form = QuestionForm(request.POST or None)
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return render(request, 'study/question.html', self.get_context_data())





    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.object_list = self.get_queryset()
    #     self.form = self.get_form(self.form_class)
    #
    # def get(self, request, *args, **kwargs):
    #     # From ProcessFormMixin
    #     form_class = self.get_form_class()
    #
    #     if self.request.method == 'POST':
    #         if self.form.is_valid():
    #             self.form.save()
    #
    #             return reverse_lazy('question')
    #
    #     else:
    #         self.form_class(self.request.POST)
    #
    #         # return super(ProductListView, self).form_valid(form)
    #
    #     # From BaseListView
    #     allow_empty = self.get_allow_empty()
    #     if not allow_empty and len(self.object_list) == 0:
    #         raise Http404("Empty list")
    #
    #     context = self.get_context_data(object_list=self.object_list, form=self.form)
    #     return self.render_to_response(context)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.get(request, *args, **kwargs)


def question_form(request):
    form = QuestionForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('contact')
    if request.is_ajax():
        form = QuestionForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return reverse_lazy('question')


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная',
    }
    return render(request, 'study/home.html', context)


def about(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Обо мне',
    }
    return render(request, 'study/about.html', context)


def contact(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Свяжитесь со мной',
    }
    return render(request, 'study/contact.html', context)


# def question(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Вопросы и ответы',
#     }
#     return render(request, 'study/question.html', context)


# def review(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Отзывы',
#     }
#     return render(request, 'study/review.html', context)


# def blog(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#         'title': 'Блог',
#     }
#     return render(request, 'study/blog.html', context)


# def post(request, post_slug):
#     single_post = get_object_or_404(Post, slug=post_slug)
#     context = {'post': single_post}
#     return render(request, 'study/post.html', context)


def price(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Прайс-лист',
    }
    return render(request, 'study/price.html', context)


def personal(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Блог',
    }
    return render(request, 'study/personal.html', context)
