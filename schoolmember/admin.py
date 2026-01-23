from django.contrib import admin

from .models import SchoolMember

# Register your models here.
class SchoolMemberAdmin(admin.ModelAdmin):
    list_display = ("memberName", "memberDesignation", "member_type", "memberDepartment", "memberEmail", "memberPhone", "memberImage", "memberApprove",)
    list_filter = ("memberEmail", "memberDesignation", )
    search_fields = ("memberEmail", "memberDesignation", )
    
admin.site.register(SchoolMember, SchoolMemberAdmin)
