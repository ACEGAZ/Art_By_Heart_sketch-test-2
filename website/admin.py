from django.contrib import admin
from .models import add_art
from .models import comment
from .models import regular_commission

admin.site.register(regular_commission)
admin.site.register(add_art)
admin.site.register(comment)