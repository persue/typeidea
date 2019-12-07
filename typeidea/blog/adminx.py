import xadmin
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter
import requests
#from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_permission_codename

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm
#from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

#PERMISSION_API = "http://permission.sso.com/has_perm?user={}&perm_code={}"


class PostInline:
    form_layout = (
        Container(
            Row("title","desc"),
        )
    )

    extra = 1
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'
    '''
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list(
            'id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset
    '''

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin,
                         field_path)

        self.lookup_choices = Category.objects.filter(
            owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    list_filter = [
        'category',
    ]

    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ), 
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        )
    )
    #filter_horizontal = ('tag',)
    #filter_vertical = ('tag', )


    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>',
                           reverse('xadmin:blog_post_change', args=(obj.id, )))

    operator.short_description = '操作'

    '''
    @property
    def media(self):
        media = super().media()
        media.add_js([
            'https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'
        ])
        media.add_css({
            'all':
            ("https://cdn.bootcss.com/bootstrap/4.0.0-beta2/css/bootstrap.min.css",
             ),
        })
        return media
		

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


    def has_add_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('add', opts)
        perm_code = "%s.%s" % (opts.app_label, codename)
        resp = requests.get(PERMISSION_API.format(request.user.username,  perm_code))

        if resp.status_code == 200:
            return True
        else:
            return False
    '''

'''
@xadmin.sites.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'object_repr', 'object_id', 'action_flag', 'user', 'change_message'
    ]
'''