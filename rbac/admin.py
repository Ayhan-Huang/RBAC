from django.contrib import admin
from .models import Menu, Permission, Role, UserInfo

# Register your models here.
admin.site.register(Menu)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserInfo)