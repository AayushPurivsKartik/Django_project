from django.contrib import admin
from .models import Member

# Register your models here.
# 1st way
# admin.site.register(Member)
# 2nd way
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(Member, MemberAdmin)