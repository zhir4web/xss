from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    path('feedback/', views.feedback, name="feedback"),
    path('feedbacks/list/', views.feedback_list, name="feedback_list"),
    path('<slug:slug>', views.post_page, name="page"),
]