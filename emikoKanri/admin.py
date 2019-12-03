# Register your models here.
from django.contrib import admin
from .models import Post
from .models import NurseRecord

admin.site.register(Post)
admin.site.register(NurseRecord)
