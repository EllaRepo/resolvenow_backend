from django.contrib import admin
from api.models import User, Inspector, Profile, Complaint, CompTypes, Region

class InspAdmin(admin.ModelAdmin):
    list_display = ['email', 'region', 'sector']

class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name','username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'verified']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'compType']

class CompTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(User, UserAdmin)
admin.site.register(Inspector, InspAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Complaint,ComplaintAdmin)
admin.site.register(CompTypes, CompTypesAdmin)
admin.site.register(Region, RegionAdmin)