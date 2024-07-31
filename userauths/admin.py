from django.contrib import admin
from userauths import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'phone')
  # list_editable = ['phone']
  search_fields = ['full_name']
  list_filter = ['phone']

class ProfileAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'gender', 'country')
  # list_editable = ['gender', 'country']
  search_fields = ['full_name']
  list_filter = ['date']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
