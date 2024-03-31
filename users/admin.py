from django.contrib import admin

# from users.models import User
#
# admin.site.register(User)

from users.models import User


# Register your models here.
# регистрируем группу на сайте - это на лайве

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('password',)
