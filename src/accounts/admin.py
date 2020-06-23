from django.contrib import admin
from .models import User, Bcrypt

class BcryptAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

admin.site.register(User)
admin.site.register(Bcrypt, BcryptAdmin)
