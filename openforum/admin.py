"""
Admin Configuration
"""

from django.contrib import admin
from .models import User, Question, Answer, Comment, Configuration

# Register models with admin console.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Configuration)