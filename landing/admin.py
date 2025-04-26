from django.contrib import admin
from .models import Article,Product,Appointment,Cart

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('-id',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Cart)

# admin.site.register(Article)