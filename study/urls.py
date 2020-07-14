from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('question/', Questions.as_view(), name='question'),
    # path('question-form/', question_form, name='question-form'),
    path('review/', Reviews.as_view(), name='review'),
    path('blog/', Posts.as_view(), name='blog'),
    path('blog/<str:slug>/', SinglePost.as_view(), name='post'),
    path('price/', price, name='price'),
    path('personal/', personal, name='personal'),
]
