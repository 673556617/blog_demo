#!/usr/bin/python
# coding:utf-8
from django.contrib import admin
from zard.models import Author, Article, Tag,Classification, Music, Site
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')  #设置作者类显示的表头
    search_fields = ('name',)                    #添加按姓名查询的功能

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'id', 'author', 'publish_time','classification')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'        #设置时间过滤器
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)         #水平显示的过滤器
#以上内容均为对显示内容的修饰

#因为没有更新视图
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name','path','address','album','artist')
    list_filter = ('album',)

class SitesAdmin(admin.ModelAdmin):
    list_display = ('name','longitude','lattitue','picSrc','description','author','caption')
    list_filter = ('author',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Classification)

admin.site.register(Music,MusicAdmin)
admin.site.register(Site,SitesAdmin)
