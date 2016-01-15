from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,render_to_response,RequestContext
from zard.models import  Article,Classification,Site
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib.auth import  logout
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict

from django.views.generic.edit import FormView

from forms import ArticlePublishForm,ArticlePublishForm2

from markdown import markdown
import json
# Create your views here.
#class SitesEncoder(json.JSONEncoder):


def index(request):
    # articles = Article.objects.all()
    # classifications = Classification.objects.all()

    sites = list(Site.objects.all().values())
    #print sites
    mark1 = ['aa', 'aa33']
    Dict = {'site': 'aa', 'author': 'aa'}
    address = "{% static '/music' %}"
    context = { 'mark1': json.dumps(mark1),'Dict':Dict,'sites':json.dumps(sites)}
    return render(request,'new_blog/index.html',context)

def marks(request):
    context={}
    return render(request,'multiplemark.html',context)

def content(request, id):
    article = get_object_or_404(Article,id = id)


    context = {"article":article}
    return render(request,'blog/content.html',context)

def dropup(request):
    contenxt={}
    return render(request,'new_blog/dropup.html',contenxt)

def login(request):
    contenxt={}
    return render(request,'new_blog/login.html',contenxt)
def signin(request):
    #userlist= User.objects.all()
    #print userlist
    #use authentification

    c={}
    c.update(csrf(request))

    inputUsername=  request.POST.get('inputUsername',False)
    inputPassword = request.POST.get('inputPassword',False)
    #print inputUsername
    #print inputPassword
    user = auth.authenticate(username=inputUsername, password=inputPassword)
    if user is not None and user.is_active:
        print "login ok"
        #login(request, user)
        auth.login(request, user)
        context={"user":user,"islogin":True}
        #return HttpResponseRedirect('/')
        return render(request,'new_blog/index.html',context)
    else:
        errormsg = "username or password invalid"
        c = {"errormsg":errormsg}

        return render_to_response('new_blog/login.html',RequestContext(request, c))
    # contenxt={}
    # return render(request,'new_blog/login.html',contenxt)
    #return HttpResponseRedirect('index')

def article(request,caption):
    # use below to get article information
    article = Article.objects.get(caption = caption)
    #what the boner?
    article.content = markdown(article.content)
    print article.caption
    context={"article":article}
    return render(request,'new_blog/article.html',context)
def logoff(request):
    logout(request)
    print 'logout...'
    return HttpResponseRedirect('/')

def articles(request):
    articles = Article.objects.all()
    for article in articles:
        article.content = markdown(article.content)
    context={"articles": articles}

    return render(request,'new_blog/articles.html',context)


class ArticlePublishView(FormView):
    template_name = 'new_blog/publish_article.html'
    form_class = ArticlePublishForm
    success_url = '/blog/'

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView, self).form_valid(form)
class ArticlePublishView2(FormView):
    template_name = 'new_blog/publish_article2.html'
    form_class = ArticlePublishForm2
    success_url = '/'

    def form_valid(self, form):
        form.save(self.request.user.username)
        return super(ArticlePublishView2, self).form_valid(form)