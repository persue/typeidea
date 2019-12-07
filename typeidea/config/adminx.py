import xadmin

#from django.contrib import admin

# Register your models here.
from .models import Link, SideBar
#from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

@xadmin.sites.register(Link) #question
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')
