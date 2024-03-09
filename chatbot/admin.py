

# Register your models here.
# chatbot/admin.py
from django.contrib import admin
from .models import Question, Response

admin.site.register(Question)
admin.site.register(Response)
