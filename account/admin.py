from django.contrib import admin
from .models import Relation, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    verbose_name = 'Profile'



class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)



admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)




@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    pass

