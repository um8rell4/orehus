from django.contrib import admin
from .models import OrehusChange, CustomUser, UserZodiacSign


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'rating')


class UserZodiacSignAdmin(admin.ModelAdmin):
    list_display = ('zodiac_sign', 'zodiac_sign')


class OrehusUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')


class OrehusChangeAdmin(admin.ModelAdmin):
    list_display = ('comment', 'operation', 'datetime_comment', 'orehus_user')


admin.site.register(OrehusChange, OrehusChangeAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserZodiacSign, UserZodiacSignAdmin)
