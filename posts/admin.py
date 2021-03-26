from django.contrib import admin
from .models import Post



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('pk','user','profile','title','created')
    search_fields=('pk','user')
    