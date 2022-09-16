from django.contrib import admin
from .models import add_art
from .models import Comment


admin.site.register(add_art)
admin.site.register(Comment)
