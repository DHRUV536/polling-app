from django.contrib import admin
from .models import Contact, Polls
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'subject', 'time', 'solved']
    list_filter = ['solved','time']
    list_editable = ['solved']
    search_fields=('name','subject')

@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'create_time']
    
    list_filter = ['create_time']
    search_fields=('title','descrption')

