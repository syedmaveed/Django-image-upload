

from feed.models import Post
from  .models import Post
from django.contrib import admin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)