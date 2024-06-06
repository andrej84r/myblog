from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_html_image', 'title', 'rubric', 'time_create', 'time_update', 'publication']
    list_editable = ['publication']
    readonly_fields = ['get_html_image', 'time_create', 'time_update']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 15

    def get_html_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=100>")

    get_html_image.short_description = "Miniature"

