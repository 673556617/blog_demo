#!/usr/bin/env python
# coding=utf-8

import datetime
import re
import markdown
from django.db import models
from django import forms
from models import Article,Classification,Tag,Author
from django.contrib.auth.models import User

class ArticlePublishForm(forms.Form):
    title = forms.CharField(
        label=u'文章标题',
        max_length=200,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'文章标题，记得在标题末尾添加".html"'}),
        )

    content = forms.CharField(
        label=u'内容',
        min_length=10,
        widget=forms.Textarea(),
        )

    tags = forms.CharField(
        label=u'标签',
        max_length=400,
        widget=forms.TextInput(attrs={'class': '', 'placeholder': u'文章标签，以空格进行分割'}),
        )

    def save(self, username):
        cd = self.cleaned_data
        title = cd['title']
        title_zh = title
        now = datetime.datetime.now()
        content_md = cd['content']
        content_html = markdown.markdown(cd['content'])
        re_title = '<h\d>(.+)</h\d>'
        data = content_html.split('\n')
        for line in data:
            title_info = re.findall(re_title, line)
            if title_info:
                title_zh = title_info[0]
                break
        url = '/article/%s' % (title)
        tags = cd['tags']
        # article = Article(
        #     url=url,
        #     title=title,
        #     title_zh=title_zh,
        #     author=username,
        #     content_md=content_md,
        #     content_html=content_html,
        #     tags=tags,
        #     views=0,
        #     created=now,
        #     updated=now)
        # article.save()


class ArticlePublishForm2(forms.Form):
    caption = forms.CharField(max_length=50)
    #author = models.ForeignKey(Author)  get from session
    #tags = models.ManyToManyField(Tag,blank=True)  complicated: print radio and all
    #classification = models.ForeignKey(Classification) complicated: similar
    content = forms.CharField(
        label=u'内容',
        min_length=10,
        widget=forms.Textarea(),
        )

    def save(self, username):
        cd = self.cleaned_data
        # print "caption:",cd['caption']
        # print "content:",cd['content']
        # user = User.objects.get(username=username)
        # print user.username
        user = User.objects.get(username=username)
        curcaption = cd['caption']
        curcontent = markdown.markdown(cd['content'])
        curauthor = Author.objects.get(name = username)

        curclassification = Classification.objects.get(name = "旅游")
        article = Article(author =curauthor, caption = curcaption, content=curcontent,classification=curclassification )
        article.save()




