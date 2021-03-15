from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'
	list_display = ('title','slug','status','uploaded_on')
	list_filter = ('status',)
	search_fields = ['title','slug','content']
	prepopulated_fields = {'slug':('title',)}