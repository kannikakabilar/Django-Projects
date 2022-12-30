from django.contrib import admin
from .models import Members

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("fullname", "soi", "email", "role",)
  
admin.site.register(Members, MemberAdmin)

