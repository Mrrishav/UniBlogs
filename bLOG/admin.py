from django.contrib import admin
from .models import Category,Post,Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','url')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page =20

    class Media():
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)




admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)