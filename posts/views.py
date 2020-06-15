from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from .filters import OrderFilter
import json
from django import forms
import datetime
from django.utils import timezone
from django.utils.timezone import utc



# Create your views here.
def posts(request):
    posts = Post.objects.filter(author_id=request.user).order_by('updated')
    return render(request, 'all_posts.html', {'posts': posts})

def selectPost(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        print(subject)
        selected_posts = Post.objects.filter(subject=subject)
        return render(request, 'all_posts.html', {'selected_posts': selected_posts})
    else:
        posts = Post.objects.filter(author_id=request.user).order_by('updated')
        return render(request, 'all_posts.html', {'posts': posts})

def writePost(request):

    if request.method == 'POST':
        description = request.POST['description']
        source = request.POST['source']
        subject = request.POST['subject']
        
        post = Post(description=description, source=source, subject=subject, seen = 0, author_id=request.user.pk)
        post.save()
        print('Post created')
        return redirect('all_posts')
        
    else:
        return render(request, 'write_post.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

#class NameForm(forms.Form):
   # id = forms.IntegerField(label='id')


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})

def dailyPosts(request):

    if request.method == 'POST':
        #Formid = request.GET.get(id)
        #thePost = Post.objects.get(pk = Formid)
        #thePost.seen += 1
        #thePost.save()
        daily_posts = Post.objects.filter(author_id=request.user).order_by('seen','-updated')[:5]
        for post in daily_posts:
            print(post.id)
            post.seen += 1
            post.save()
        #id = request.GET.get('id')
        #post = Post.objects.get(id=post_id)
        #post.seen = post.seen + 1
        #post.save()
        print('Post updated')
        return redirect('all_posts')

    else:
        daily_posts = Post.objects.filter(author_id=request.user).order_by('seen','-updated')[:5]
        return render(request, 'daily_posts.html', {'daily_posts': daily_posts})
        
        #def find_daily_posts():
        #    return render(request, 'daily_posts.html', {'daily_posts': daily_posts})
        #schedule.every(3).seconds.do(find_daily_posts) 
        #while 1:
        #    schedule.run_pending()
        #    time.sleep(1)



        #print(request)
        #print(request.POST)
        #print(request.POST['id'])
        #post_id = NameForm(request.POST)
        #print(post_id.id)
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)
        #print(body)
