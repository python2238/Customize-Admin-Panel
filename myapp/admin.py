from django.contrib import admin
from myapp.models import user

class userAdmin(admin.ModelAdmin):
    fields =['Contact','name']
    search_fields = ['name']
    list_filter = ['Contact','name']
    list_display = ['name','Contact']
    list_editable = [ 'Contact']

admin.site.register(user,userAdmin)
