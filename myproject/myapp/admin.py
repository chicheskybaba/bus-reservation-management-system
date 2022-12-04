from django.contrib import admin
from .models import Bus, User, Book

# Register your models here.





@admin.register(Bus)
class PostAdmin(admin.ModelAdmin):
    list_display = ['bus_name', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time']
    list_filter = ['bus_name', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time']
    search_fields = ['bus_name', 'source', 'dest', 'nos', 'rem', 'price', 'date', 'time']
    ordering = ('-date',)

@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'email']
    list_filter = ['user_id', 'name', 'email']
    search_fields = ['user_id', 'name', 'email']



@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'userid', 'email', 'busid', 'bus_name', 'source', 'dest', 'nos', 'price', 'date', 'time', 'status']
    list_filter = ['name', 'userid', 'email', 'busid', 'bus_name', 'source', 'dest', 'nos', 'price', 'date', 'time', 'status']
    search_fields = ['name', 'userid', 'email', 'busid', 'bus_name', 'source', 'dest', 'nos', 'price', 'date', 'time', 'status']
    ordering = ('-date',)