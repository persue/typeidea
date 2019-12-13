# -*- coding: utf-8 -*-
import xadmin

#from django.contrib import admin

from .models import Comment 
#from typeidea.custom_site import custom_site
#from typeidea.base_admin import BaseOwnerAdmin

@xadmin.sites.register(Comment)
class CommentAdmin:
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
