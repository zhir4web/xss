from django.contrib import admin
from .models import Post, Feedback

# Register your models here.
admin.site.register(Post)
# ...existing code...
admin.site.register(Feedback)