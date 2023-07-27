from django.contrib import admin

# Register your models here.
from .models import Post

#registering app
admin.site.register(Post)
