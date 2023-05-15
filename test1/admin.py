from django.contrib import admin
from .models import user_preferences

# Register your models here.
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'pref_1', 'pref_2', 'pref_3')


admin.site.register(user_preferences, UserPreferencesAdmin)
