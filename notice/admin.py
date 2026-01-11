from django.contrib import admin
from .models import Catagory, Notice

# Admin Panel Notice Data Show

# Notice Part
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("noticeTitle", "noticeDescription", "noticeCatagory", "noticeCreate", "noticeImage",)
    list_filter = ("noticeCatagory", "noticeCreate", )
    search_fields = ("noticeTitle", "noticeCatagory", )


# Catagory Part
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ("catagoryName",)
    list_filter = ("catagoryName",)

# Register your models here.
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Catagory, CatagoryAdmin)