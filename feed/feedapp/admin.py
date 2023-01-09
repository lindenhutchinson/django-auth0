from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Report

# register models so they can be viewed on the admin dashboard
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Report)
